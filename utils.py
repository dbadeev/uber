import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error


# def mae_for_df(df_true: pd.DataFrame, df_test: pd.DataFrame) -> float:
# 	"""
#
# 	:param df_true:
# 	:param df_test:
# 	:return:
# 	"""
# 	mae_lst = np.array([])
# 	for col in df_true:
# 		mae_lst = np.append(mae_lst, mean_absolute_error(df_true[col], df_test[col]))
# 	return mae_lst.mean()


def prepare_data(df: pd.DataFrame, lags_list: list):
	"""
	Формирование train/test наборов для моделей
	:param df: Датафрейм с данными
	:param lags_list: Список лагов (сдвигов) для формирования дополнительных столбцов с данными
	:return: Набор train/test
	"""

	data = pd.DataFrame(df.copy())
	data.columns = ['y']

	# добавляем лаги исходного ряда в качестве признаков
	for i in lags_list:
		# for i in [672, 1344, 2016]:
		data["lag_{}".format(i)] = data.y.shift(i)

	data = data.fillna(0)
	# data = data.reset_index(drop=True)

	# разбиваем data на тренировочную и тестовую выборку

	x_train = data.loc[:'2019-06-16'].drop(["y"], axis=1)
	y_train = data.loc[:'2019-06-16']["y"]

	x_test = data.loc['2019-06-17':'2019-06-23'].drop(["y"], axis=1)
	y_test = data.loc['2019-06-17':'2019-06-23']["y"]

	x_predict = data.loc['2019-06-24':].drop(["y"], axis=1)

	return x_train, x_test, y_train, y_test, x_predict


def update_df(df: pd.DataFrame) -> pd.DataFrame:
	"""
	В датафрейме отрицательные значения заменяются на 0, остальные значения округляются
	:param df: Исходный датафрейм
	:return: Преобразованный датафрейм
	"""

	for area in df:
		df.loc[df[area] < 0., area] = 0.
	return df.round(0)
