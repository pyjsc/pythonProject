"""
Array alt kümesine erişmek (Slicing)

"""
import numpy as np

#Tek boyutlu
array = np.arange(20,30)#20 ile 30 arasındaki sayılardan oluşmuş tek boyutlu array.
altkume = array[0::2]

#İki boyutlu

matris = np.random.randint(10,size=(5,5))
print(matris)
sutun = matris[:,0] #ilk değer tüm satırlar anlamına geliyor , ikinci değer çekmek istediğimiz sütun.
satir = matris[0,:]

#Herhangi bir elemana erişme

herhangi = matris[0:2,0:3]

herhangi2 = matris[:,0:2]

herhangi3 = matris[1:3,0:2]
