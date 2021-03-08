import seaborn as sns
import pandas as pd
#Veri setinin hikayesi nedir ? sorulması gereken ilk soru
#Veri seti Hikayesi ve yapısının incelenmesi.

planets = sns.load_dataset("planets")
ilk_gozlemler = planets.head()
df = planets.copy()


#veri seti yapısal bilgileri
bilgi = df.info()

#object tipini kategorik değişkene değiştirme
df.method = pd.Categorical(df.method)








