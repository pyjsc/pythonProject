import numpy as np
import pandas as pd

"""

v1 = np.random.randint(10, size=5)
v2 = np.random.randint(10, size=5)
v3 = np.random.randint(10, size=5)

sozluk = {"var1":v1,"var2":v2,"var3":v3}

dataframe = pd.DataFrame(sozluk)
print(dataframe)
print(dataframe[0:1])

dataframe.index = ["a","b","c","d","e"] #index isimlerini değiştirdik
print(dataframe)

#silme işlemi
dataframe.drop("a",axis=0,inplace=True) #tüm satırı siler inplace argümanının görevi yapılan işlemin kalıcı olmasını sağlar.
#inplace kullanılmadığında işlem orjinal yapıyı bozmaz.

#fancy ile silme işlemi
liste = ["c","e"]
dataframe.drop(liste,axis=0,inplace=True)
print(dataframe)

"""

#Değişkenler için


array = np.random.randint(10,size=9).reshape(3,3)
print(array)
dataframe = pd.DataFrame(array,columns=["sütun1","sütun2","sütun3"])
print(dataframe)

bool = "sütun1" in dataframe
print(bool)

liste = ["var1","var2","var3"]

for i in liste:
	print(i in dataframe)


dataframe["sütun4"] = dataframe["sütun1"] * dataframe["sütun2"] #olmayan sütunu var olan sütunlara işlem uygulayarak oluşturduk.
print(dataframe)


#Değişken silmek
dataframe.drop("sütun4",axis = 1,inplace=True)
print(dataframe)

#fancy ile silme

liste2 = ["sütun1","sütun2"]
dataframe.drop(liste2,axis=1,inplace=True)
print(dataframe)










