import pandas as pd


def is_data_frame(data):
    """
    is object data frame
    :param data: object
    :return: bool
    """
    return type(data) == pd.core.frame.DataFrame


def define_type(data):
    """
    it is just a wrapper

    :param data: DataFrame
    :return: pd series
    """
    if is_data_frame(data):
        return data.dtypes

def typedef(data: pd.DataFrame) -> dict:
    """
    return dict with types of columns of data frame
    :param data: DataFrame
    :return: dict
    """
    res = {}
    if is_data_frame(data):
        for col in data.columns:
            res[col] = str(data[col].dtypes)
    return res
