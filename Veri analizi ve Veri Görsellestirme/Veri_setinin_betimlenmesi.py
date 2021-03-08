import seaborn as sns
import pandas as pd

planets = sns.load_dataset("planets")
df = planets.copy()

#betimsel istatistikler
#describe fonksiyonu eksik gözlemleri gözardı eder ve kategorik değişkenleri dışarda bırakır.
bilgi = df.describe()


#EKSİK DEĞERLERİN İNCELENMESİ
sorgu = df.isnull().values.any() #Eksik gözlem var mı ? Varsa true yoksa false döner.
#hangi değişkende kaçar tane eksik değer var ?
sorgu2 = df.isnull().sum()

#Bütün eksik değerlerin yerine 0 basılabilir. fakat tehlikelidir.
df["orbital_period"].fillna(0, inplace = True)
sorgu3 = df.isnull().sum()

#Bütün eksik değerlerin yerine 0rtalamaları basılabilir. fakat tehlikelidir.
df["mass"].fillna(df.mass.mean(), inplace=True)
sorgu4 = df.isnull().sum()


#Tüm eksik değerlerin yerine ortalamaları basılabilir.
df.fillna(df.mean(),inplace=True)
sorgu5 = df.isnull().sum()
























