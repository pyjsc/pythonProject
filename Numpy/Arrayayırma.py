"""
Array ayırma (Splitting)

"""

import numpy as np


x = np.array([1,2,3,99,99,3,2,1])

ayrilma = np.split(x,[3,5]) # index+1  parça ayırır ... burada 2 index verdiğimiz için 3 parçaya ayırdı

#Bölünmüş arrayları tekrardan kullanma.

a,b,c = np.split(x,[3,5])

#İKİ BOYUTLU AYIRMA
#dikey olarak bölme
m = np.arange(16).reshape(4,4)
print(m)
ust,alt = np.vsplit(m,[2])
#yatay olarak bölme
sag,sol = np.hsplit(m,[2])
















