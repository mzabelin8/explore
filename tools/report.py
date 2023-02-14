import explore_warnings
import typedef

import pandas as pd
import seaborn as sns
from IPython.core.display import display, HTML, Markdown


def highlight_non_zeros(x):
    if x == 0:
        color = '#84f08f'  # green
    else:
        color = '#f299a9'  # red

    return f'background: {color}'


def to_html(data: dict):
    """
    convert dict to html using pandas
    :param data: dict
    :return: ipython.display html
    """
    pal = sns.light_palette("red", as_cmap=True)
    df = pd.DataFrame(data.items(), columns=['Cols', 'Mis values'])
    display(HTML(df.style.background_gradient(cmap=pal).to_html()))
