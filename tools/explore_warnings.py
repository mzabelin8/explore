import pandas as pd
import typedef
import report
from IPython.core.display import display


def missing_values(data, by_columns=False):
    """

    :param data: dataframe
    :param by_columns: bool
    :return: dict or int
    """
    if typedef.is_data_frame(data):
        if by_columns:
            res = dict(data.isna().sum())
            display(report.to_html(res))
            return res
        res = {'mis values': data.isna().sum().sum()}
        return res
