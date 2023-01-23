import explore_warnings
import typedef

import pandas

import seaborn as sns

data = sns.load_dataset('titanic')
print(explore_warnings.missing_values(data, True))
print(explore_warnings.missing_values(data))
