import pandas as pd


def is_data_frame(data):
    return type(data) == pd.core.frame.DataFrame


def typedef(data: pd.DataFrame) -> dict:
    res = {}
    if is_data_frame(data):
        for col in data.columns:
            res[col] = str(data[col].dtypes)
    return res
