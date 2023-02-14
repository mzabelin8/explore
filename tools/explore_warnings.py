import pandas as pd
import typedef
import report
from IPython.core.display import display
import numpy as np


def get_cols_names(data):
    """
    it is just a wrapper

    :param data: DataFrame
    :return: pd series
    """
    if typedef.is_data_frame(data):
        return data.columns


def mis_vals(data):
    """
    it is just a wrapper

    :param data: DataFrame
    :return: pd series
    """
    if typedef.is_data_frame(data):
        return data.isna().sum()


def zero_vals(data):
    """
    it is just a wrapper

    :param data: DataFrame
    :return: pd series
    """
    if typedef.is_data_frame(data):
        return (data == 0).sum()


def inf_vals(data):
    """
    it is just a wrapper

    :param data: DataFrame
    :return: pd series
    """
    if typedef.is_data_frame(data):
        return (data == np.inf).sum() + (data == -np.inf).sum()


def outlier(data, th=0.95):
    if not typedef.is_data_frame(data):
        return None

    numeric = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    res = []
    for col in data.columns:
        if data[col].dtype in numeric:
            q = data[col].quantile(th)
            res.append((data[col] > q).sum())
        else:
            res.append(0)
    return pd.Series(res, index=data.columns)


def pipeline(data):
    """
    apply all features to data and get DataFrame

    :param data: DataFrame
    :return: DataFrame
    """
    if not typedef.is_data_frame(data):
        return None

    names = get_cols_names(data)
    mis_v = mis_vals(data)
    inf_v = inf_vals(data)
    zeros = zero_vals(data)
    col_types = typedef.define_type(data)
    outl = outlier(data, 0.99)
    print(type(zeros))
    print(type(outl))

    df = pd.DataFrame({
        'Types': col_types,
        'Mis vals': mis_v,
        'Inf vals': inf_v,
        'Zero vals': zeros,
        'Outliers': outl})

    apply_to = ['Mis vals', 'Inf vals', 'Zero vals', 'Outliers']

    return df.style.applymap(report.highlight_non_zeros, subset=apply_to)
