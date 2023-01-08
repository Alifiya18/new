import pandas as pd
import numpy as np
download_url = ("file:///C:/Users/%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BE400/Desktop/%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0/Python/3%20%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D0%B5%2012.12.2022%D0%B3/dz%20(1).csv")
df = pd.read_csv(download_url, delimiter = ';|,', engine='python')
frame = pd.DataFrame(df)
print(frame)
print(frame['CTR'])

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
download_url = ("file:///C:/Users/%D0%BC%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BE400/Desktop/%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0/Python/3%20%D0%B7%D0%B0%D0%BD%D1%8F%D1%82%D0%B8%D0%B5%2012.12.2022%D0%B3/dz%20(1).csv")
df = pd.read_csv(download_url, delimiter = ';|,', engine='python')
frame = pd.DataFrame(df)
print(frame)
print(frame['CTR'])
mas_kol_klik = np.array(frame['Количество кликов'].tolist())
mas_kol_pokaz= np.array(frame['Количетсво показов'].tolist())
plt.plot(mas_kol_pokaz,mas_kol_klik)
plt.show()


