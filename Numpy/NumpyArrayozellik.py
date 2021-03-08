"""
*****Numpy array özellikleri*****

ndim : boyut sayısı
shape : boyut bilgisi
size : toplam elaman sayısı
dtype: array veri tipi
"""

import numpy as np

#TEK BOYUTLU ARRAY
array = np.random.randint(10,size=10)

boyut = array.ndim   #boyut sayısı
boyutbilgisi = array.shape  #boyut bilgisi
elemansayisi = array.size  #eleman sayısı
veritipi = array.dtype  #veri tipi


#İKİ BOYUTLU ARRAY

array2 = np.random.randint(10,size = (3,5))

boyut2 = array2.ndim
boyutbilgisi2 = array2.shape
elemansayisi2 = array2.size
veritipi2 = array2.dtype





