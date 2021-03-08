"""
Histogram ve Yogunluk Grafiği

--Sayısal değişkenlerin dağılımını ifade etmek için kullanılan veri görselleştirme teknikleridir.


"""


import seaborn as sns
import matplotlib.pyplot as plt
diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()
"""
#sadece histogram grafiği
sns.distplot(df.price,kde=False)#dağılım görselleştirmek için kullanılan fonksiyon

#histogram üzerine yoğunluk
sns.distplot(df.price,kde=True)

#sadece yogunluk grafiği
sns.distplot(df.price,hist=False,kde=True)
"""
#sadece yogunluk grafiği ve altının doldurulması
sns.kdeplot(df.price,shade=True)
plt.show()


