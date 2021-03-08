import pandas as pd
import numpy as np

df = pd.DataFrame({"gruplar":["A","B","C","A","B","C"],
                   "degisken1":[10,23,33,22,11,99],
                   "degisken2":[100,253,333,262,111,969]})


#Aggregate fonksiyonu ---- GRUPLARA GÖRE HESAPLAMA İŞLEMLERİ
grup = df.groupby("gruplar").mean() #eski yöntem tek bir hesabı yapıyor.
#yeni yöntemler
grup2 = df.groupby("gruplar").aggregate([min,np.median,max])
grup3 = df.groupby("gruplar").aggregate({"degisken1":min,"degisken2":max})

#Filter fonksiyonu
def filter_func(x):
	return x["degisken1"].std() > 9  #standart sapması 9 dan büyük olanları döndürür.

filter = df.groupby("gruplar").filter(filter_func) #tanımladığımız fonksiyonu filter fonksiyonuna gönderdik.


#Transform fonksiyonu -------DÖNÜŞTÜRME İŞLEMLERİ
df_a = df.iloc[:,1:3] #KATEGORİK DEĞİŞKENİ VERİ SETİNDEN ÇIKARDIK.
donusum = df_a.transform(lambda x: (x-x.mean()) / x.std() )

#Apply fonksiyonu

df2 = pd.DataFrame({"degisken1":[10,23,33,22,11,99],
                    "degisken2":[100,253,333,262,111,969]})

donusum2 = df2.apply(np.sum)


df3 =pd.DataFrame({"gruplar":["A","B","C","A","B","C"],
                   "degisken1":[10,23,33,22,11,99],
                   "degisken2":[100,253,333,262,111,969]})

donusum3 = df3.groupby("gruplar").apply(np.mean)
print(donusum3)








