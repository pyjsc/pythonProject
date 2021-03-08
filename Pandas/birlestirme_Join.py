import pandas as pd
import numpy as np

array = np.random.randint(1,30, size=(5,3))
dataframe = pd.DataFrame(array, columns=["var1","var2","var3"])

dataframe2 = dataframe + 99
dataframe2.columns = ["var1","var2","degisken1"]

#birleştirme işlemi
birlesim = pd.concat([dataframe,dataframe2],ignore_index=True,join="inner")
"""
ignore_index metodu : True olduğunda indexleri sıfırdan yazar.
join metodu : birleştirme işlemini kesişimlerine göre birleştirir. 
"""
print(birlesim)

birlesim2 = pd.concat([dataframe,dataframe2],axis=0)
print(birlesim2)
