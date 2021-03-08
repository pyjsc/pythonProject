import numpy as np
#TEK BOYUTTA FANCY
v = np.arange(0,30,3)

indexleri_al = [2,6,8]
alinandegerler = v[indexleri_al]

#İKİ BOYUTTA FANCY

matris = np.arange(9).reshape((3,3))
print(matris)
satir = np.array([0,1])
sutun = np.array([1,2])

alinandegerler2 = matris[satir,sutun]

#Basit index ile fancy index

secim = matris[0,[1,2]]#0.satırı al 1 ve 2. sütunu al

#Slice ile fancy index

secim2 = matris[:,[1,2]]#bütün satıları al ve 1ve2sütunu al.






