import pandas as pd
import numpy as np

array = np.array([11,22,23,24,55])
seri = pd.Series(array,index=["a","b","c","d","e"])
"""
print(seri)
print(seri.index)#serinin index adlarını bastırır.
print(seri.keys)#serinin anahtarları
print(list(seri.items()))#serinin index ve anahtarları
"""

#eleman sorgulama
bool = "f" in seri # "f" ifadesi serinin içinde mi ?
print(bool)#True veya false
print(seri["a"]) #"a" indexinin tuttuğu değer döner

#fancy eleman sorgulama
print(seri[["a","b","c"]])

#değer değiştirme
seri["a"] = 444
print(seri)

#Slice ile eleman sorgulama
print(seri["a":"c"])
