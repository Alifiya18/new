import matplotlib.pyplot as plt
import seaborn as sns
x = ['Сургут', 'Ханты-Мансийск', 'Тюмень', 'Казань', 'Москва']
y = [58, 60,43, 42, 117]
sns.barplot(x=x, y=y,  color = 'black')
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(20).cumsum(), index=np.arange(0,100,5))
s = pd.Series([12,-4,7,9,17], [0,2,10,-1, 8])
s.plot(xlim = [-30,30], ylim = [-30,30], style = 'd--', alpha = 0.6, kind = 'line', logy = 1, use_index = 0, xticks = [0,5,10,15,20,25,30,-5,-10,-15,-20,-25,-30],  rot = 30, yticks = [0,2,10,12,20,22,30,-2,-10,-12,-20,-22,-30], grid = 1)
plt.show()