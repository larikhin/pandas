import pandas as pd
import numpy as np

scores3 = [{'Name column':'mat2','Data1':7, 'Data2':9},
        {'Name column':'mat2','Data1':9},
        {'Name column':'fizic2','Data1':7}]
my_df3 = pd.DataFrame(scores3)
print(my_df3)
print(my_df3.head(1))
print(my_df3.tail(2))

