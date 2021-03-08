import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

planets = sns.load_dataset("planets")
df = planets.copy()

#Sadece kategorik değişkenleri çekmek ve özetleri

kat_df = df.select_dtypes(include=["object"])#istediğimiz tipe göre değişken çekmek için kullanılır.

#Kategorik degişkenin sınıflarına ve sınıf sayısına erişmek
sinif_bilgileri = kat_df.method.unique()
sayisi = kat_df["method"].value_counts().count()

#Kategorik değişkenin sınıflarının frenkanslarına erişmek
##Frekans : tekrarlama sayısı
frekans = kat_df["method"].value_counts()


#Temsili görselleştirme
df["method"].value_counts().plot.barh()
plt.show()

