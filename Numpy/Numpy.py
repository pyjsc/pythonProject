#NumPy array oluşturma

import numpy as np

array = np.array([1,2,3,4,5])

array2 = np.array([3.14,4,2,13],dtype="int") #hepsini integer e çevirir.

#SIFIRLARDAN OLUŞAN ARRAY OLUŞTURMA

array3 = np.zeros(10,dtype=int)


#BİRLERDEN OLUŞAN ARRAY OLUŞTURMA

array4 = np.ones((3,5),dtype= int) # 3 satır 5 sütun


#Herhangi bir sayıdan oluşan array oluşturma

array5 = np.full((3,5),3) #3 satır 5 sütun ve sadece 3 lerden oluşan 2 boyutlu array

#Doğrusal array oluşturma

array6 = np.arange(0,31,3) #0 dan 31 e kadar 3 er 3 er artan array.

#İki değer arasında belirli sayıda array oluşturma

array7 = np.linspace(0,1,10)

#İstediğimiz dağılım özelliği gösteren array

array8 = np.random.normal(10, 4,(3,4))


#Rastgele oluşturulmuş ve sadece integerlardan oluşan array.

array9 = np.random.randint(0,10,(3,3))
