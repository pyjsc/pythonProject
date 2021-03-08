#Dağılım grafikleri
"""
Verinin hikayesi ve verinin görselleştirmeye hazır hale gelmesi.
"""

import seaborn as sns
diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()

#Veri setine hızlı bakış

#gerekli bilgilere erişilmesi
df.info()

#verinin betimsel özelliklerine erişilmesi (ortalama,max-min değer , standart sapma vb.)
ozellik = df.describe()
print(ozellik)

#ordinal tanımlama
from pandas.api.types import  CategoricalDtype

cut_kategoriler = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories=cut_kategoriler,ordered=True)) #Belirtilmiş olan kategorik değişkenin tipini değiştir ve sıralı yani ordinal birşekilde yap.
print(df.cut.head(1))




