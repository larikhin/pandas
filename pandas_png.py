import pandas as pd


df = pd.DataFrame({'A':range(100)})
the_plot_array = df.hist(column = 'A')
fig = the_plot_array[0][0].get_figure()
fig.savefig('output.png')
