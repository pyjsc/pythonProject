import pandas as pd

#seri oluşturma
seri = pd.Series([1,2,3,4,5])#serinin değerleri ve indexleri beraber tutulur.

"""
print(seri.axes)#serinin indexleri
print(seri.dtype)#serinin tipi
print(seri.size)#eleman sayısı
print(seri.ndim)#boyut sayısı
print(seri.values)#sadece değerler
print(seri.head(3))#serinin 3 gözlemini(değerini) getirir.(Baştan bakmak)
print(seri.tail(3))#serinin 3 gözlemini(değerini) getirir.(Sondan bakmak)
"""

#İndex isimlendirmesi
seri2 = pd.Series([101,102,444,333,222], index=[1,3,5,7,9])#indexleri isimlendirdik
print(seri2)

#String değerler ile isimlendirme
seri3 = pd.Series([112,110,155,176,911],index=["a","b","c","d","e"])
print(seri3)


#Seriler üzerinde seçme işlemi (Slice ile)
seri8 = pd.Series([1,2,3,4,5])
print(seri8[0::2])



#Sözlük üzerinden seri oluşturmak
seri4 = pd.Series({"reg":10,"log":11,"cart":12})
print(seri4)
#farklı bir oluşturma yöntemi
sozluk = {"red":10,"black":15,"yellow":18}
seri5 = pd.Series(sozluk)
print(seri5)

#İki seriyi birleştirerek seri oluşturma
seri10 = pd.concat([seri4,seri5])
print(seri10)








