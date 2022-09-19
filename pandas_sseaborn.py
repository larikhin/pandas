import matplotlib.pyplot as plt

import seaborn as sns

# sets the default style for plotting

sns.set_style("darkgrid")

titanic_data = sns.load_dataset('titanic')

titanic_data.head()
