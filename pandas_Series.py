import pandas as pd
import numpy as np


list_data = [10,20,30,40,50]
my_array = np.array(list_data)
my_series=pd.Series(my_array)
print(my_series)


list_indexes =  ["num1", "num2", "num3", "num4", "num5"]
my_series = pd.Series(my_array, index=list_indexes)
print(my_series)


my_series = pd.Series([1,2,3,4,5], index=[11,12,13,14,15])
print(my_series)

my_series = pd.Series(25,index=['a','b','c','d'])
print(my_series)


my_dict = {'a':100, 'b':200}
my_series = pd.Series(my_dict)
print(my_series)

#accessing
print(my_series[0])
print(my_series['a'])

my_list = [1,2,3,9,5,6,33,4,5]
my_series = pd.Series(my_list)
min_value = np.min(my_series)
max_value = np.max(my_series)
print(min_value, max_value) #without ()

print(my_series.mean())
print(my_series.median())
print(my_series.dtype)

#convert from series to list
my_list = my_series.tolist()
print(my_list)

print('\nall is ok')
