import pandas as pd
import typedef


def missing_values(data, by_columns=False):
    if typedef.is_data_frame(data):
        if by_columns:
            return data.isna().sum()
        return data.isna().sum().sum()



