"""
count()
first()
last()
mean()
median()
min()
max()
std()
var()
sum()
"""
import pandas as pd
import seaborn as sns

dataframe = sns.load_dataset("planets")
ilkgozlem = dataframe.head()

#ortalama
ortmass = dataframe["mass"].mean()

#(değişken içerisinde) kaç değer var ?
say = dataframe["mass"].count()

#minimum-maximum değer bulma
min = dataframe["mass"].min()
max = dataframe["mass"].max()

#Değişken içerisindeki değerlerin toplamı
toplam = dataframe["mass"].sum()

#Standart sapmasını bulma
standsapma = dataframe["mass"].std()

#varyans bulma
varyans = dataframe["mass"].var()

#Tüm istatiksel bilgileri almak için
istatiksel = dataframe.describe()
istatiksel2 = dataframe.describe().T

#eksik gözlemler varsa
dataframe.dropna().describe()