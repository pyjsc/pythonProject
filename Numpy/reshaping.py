"""
Var olan numpy array ini yeniden şekillendirme.

Vektör : Tek boyutlu array
Matris : İki boyutlu array
"""

import numpy as np

array = np.arange(1,10)
#bu array üzerinden 3 e 3 üçlük array oluşturma
#Yani tek boyutu 2 boyuta çevirdik.
donusmusarray = array.reshape(3,3)

#array in boyutu değişsin ama yapısı değişmesin

donusmusarray2 = array.reshape((1,9))
print(donusmusarray2)

