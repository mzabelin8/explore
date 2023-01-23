import pandas as pd


def typedef(data: pd.DataFrame) -> dict:
    res = {}
    if type(data) == pd.core.frame.DataFrame:
        for col in data.columns:
            res[col] = str(data[col].dtypes)
    return res
