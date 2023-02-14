import explore_warnings
import typedef

import pandas
from IPython.core.display import display, HTML, Markdown

import seaborn as sns

def misva(data):
    if typedef.is_data_frame(data):
        col_names = data.columns()



