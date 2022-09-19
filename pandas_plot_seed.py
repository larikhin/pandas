import numpy as np
import pandas as pd
# импортируем библиотеку datetime для работы с датами
import datetime
from datetime import datetime, date
# Задаем некоторые опции библиотеки pandas, которые
# настраивают вывод
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 60)
# импортируем библиотеку matplotlib для построения графиков
import matplotlib.pyplot as plt
#%matplotlib inline
# задаем стартовое значение для генератора
# случайных чисел
seedval = 111111

# генерируем временной ряд на
# основе случайного блуждания
np.random.seed(seedval)
s = pd.Series(np.random.randn(1096),
index=pd.date_range('2012-01-01', '2014-12-31'))
walk_ts = s.cumsum()
# эта строка визуализирует случайное блуждание - так просто :)
walk_ts.plot()
plt.show()
