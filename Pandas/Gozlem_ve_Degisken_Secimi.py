import numpy as np
import pandas as pd


array = np.random.randint(1,30,size=(10,3))
dataframe = pd.DataFrame(array,columns=["var1","var2","var3"])
print(dataframe)

#Loc ve Iloc kavramı

"""
Loc :  Tanımlandığı şekliyle seçim yapmak için kullanılır.
iloc:  Alışık olduğumuz indexleme mantığıyla seçim yapar.
"""
loc = dataframe.loc[0:3]
iloc = dataframe.iloc[0:3]


#fancy ve slice ile loc ve iloc
iloc1 = dataframe.iloc[1,1]
print(iloc1)
iloc2 = dataframe.iloc[:3,:2]
print(iloc2)

loc1 = dataframe.loc[0:3,"var3"]
print(loc1)