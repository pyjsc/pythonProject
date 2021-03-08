import numpy as np
import pandas as pd

array = np.random.randint(1,30, size=(10,3))
dataframe = pd.DataFrame(array, columns=["var1","var2","var3"])
print(dataframe)


sutun1 = dataframe[dataframe.var1 > 15]

hepsi = dataframe[(dataframe.var1 > 15) & (dataframe.var2 < 10)]
print(hepsi)


secim = dataframe.loc[(dataframe.var1 > 15),["var1","var2"]]
print(secim)

secim2 = dataframe[(dataframe.var1 > 15)][["var1","var2"]]
print(secim2)