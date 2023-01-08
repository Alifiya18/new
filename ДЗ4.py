import matplotlib.pyplot as plt
import numpy as np

x = np.linspace (-10,10)
y = [1/i for i in x]
plt.title("Гипербола")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x,y)
plt.show()

import pandas as pd

table = pd.DataFrame([['Яндекс (Москва)',789,'№123'],
['Яндекс (Казань)',543,'№342'],
['Яндекс (Екатеринбург)',450,'№567']],
columns = ['Office','Stuff', 'Number'])
frame = pd.DataFrame(table)
Result = frame.query('Stuff > 700 & Number < "№350"')
print(table)
print(Result)