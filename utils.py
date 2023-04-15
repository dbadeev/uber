import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error


def mae_for_df(df_true: pd.DataFrame, df_test: pd.DataFrame) -> float:
    """
    
    :param df_true: 
    :param df_test: 
    :return: 
    """
    mae_lst = np.array([])
    for col in df_true:
        mae_lst = np.append(mae_lst, mean_absolute_error(df_true[col], df_test[col]))
    return mae_lst.mean()
