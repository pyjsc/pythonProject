"""
Sıralama(Sorting)

"""

import numpy as np



v = np.array([2,1,4,3,5])

#Küçükten büyüğe sıralama orjin yapıyı bozmadan sıralama
siralama =  np.sort(v)
#Küçükten büyüğe yapısını bozarak sıralama
v.sort()

#iki boyutlu array üzerinde sıralama
#satırları sıralama
m = np.random.normal(20,5,(3,3)) #ilk değer ortalama, ikinci değer standart sapma.
yataysiralama = np.sort(m,axis=1) #satırsıralama
dikeysiralama = np.sort(m,axis=0) #sütunsıralama



m = np.array([1,2,3])











