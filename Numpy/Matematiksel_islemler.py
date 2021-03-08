import numpy as np

v = np.array([1,2,3,4,5])

# v -+/* 1 diyerek çeşitli matematiksel işlemler tüm elemanlara uygulanır.

#ufunc kavramı


#Toplama işlemi
degismis = np.add(v, 1) #1 ekledik

#Çıkarma işlemi
degismis2 = np.subtract(v, 1)#1 çıkardık

#Çarpma işlemi
degismis3 = np.multiply(v,4) #4 ile çarptık

#Bölme işlemi
degismis4 = np.divide(v,3) #3 e böldük

#Üslü işlemler
degismis5 = np.power(v,2)

#Bölümünden kalan bulma
degismis6 = np.mod(v,2)

#Mutlak değer alma
degismis7 = np.absolute(np.array([2,-3,-1,-8]))

#Trigonometrik fonksiyonlar
cosinus = np.cos(360)
sinus = np.sin(180)

#Logaritma işlemleri

array = np.array([10,11,12,14,100])

a = np.log(array)
b = np.log10(array)












