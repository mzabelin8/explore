import pandas as pd
import typedef


def missing_values(data, by_columns=False):
    """

    :param data: dataframe
    :param by_columns: bool
    :return: dict or int
    """
    if typedef.is_data_frame(data):
        if by_columns:
            return dict(data.isna().sum())
        res = {}
        res['mis values'] = data.isna().sum().sum()
        return res
