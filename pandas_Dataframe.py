import pandas as pd
import numpy as np


my_df = pd.DataFrame()
print(my_df)

scores = [['math',5,5],['engl',4],['fizics',5]]

my_df = pd.DataFrame(scores)
print(my_df)

scores2 = [['mat2',7,9],['eng2',9],['fizic2',4]]
my_df2 = pd.DataFrame(scores2, columns = ['Name column', 'Data1', 'Data2'])
print(my_df2)

scores3 = [{'Name column':'mat2','Data1':7, 'Data2':9},
        {'Name column':'mat2','Data1':9},
        {'Name column':'fizic2','Data1':7}]
my_df3 = pd.DataFrame(scores3)
print(my_df3)
print(my_df3.head(1))
print(my_df3.tail(2))

print('\n')
print(my_df3.info())

print('\n')
print(my_df3.describe())
