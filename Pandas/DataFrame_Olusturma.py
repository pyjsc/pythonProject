import pandas as pd
import numpy as np

liste = [21,23,39,44,54,76]
array = np.arange(1,10).reshape(3,3)

dataframe = pd.DataFrame(array, columns = ["var1","var2","var3"])#içerisine array veya liste alabilir.


#dataframe isimlendirme

df = pd.DataFrame(array,columns=["1.sütun","2.sütun","3.sütun"])
print(df)

#sütun isimlerini değistirelim
df.columns = ("sütun1","sütun2","sütun3")
print(df)

#bazı bilgiler

print(df.axes) #satır ve sütun bilgilerini verir , index bilgilerinide verir.
print(df.shape) #boyut bilgisi
print(df.ndim) #boyut sayısı
print(df.size) #eleman sayısı
print(df.values) #Değerlere erişmek. dönen veritin tipi numpy array idir !
print(df.head())#baştan gözlemler(değerler)
print(df.tail())#sondan gözlemler(değerler)



a = np.array([1,2,3,4,5,6,7,8,9,0])
fr2 = pd.DataFrame(a,columns=["sütun"])
print(fr2)



