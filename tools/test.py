import explore_warnings
import typedef

import pandas
from IPython.core.display import display, HTML, Markdown

import seaborn as sns

data = sns.load_dataset('titanic')
print(type(explore_warnings.missing_values(data, True)))
print(explore_warnings.missing_values(data))



