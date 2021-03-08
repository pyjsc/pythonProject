#Barplot tekniği (Sütun grafiği) elimizdeki kategorik değişkenleri gözlemlemek için kullanılır .
import seaborn as sns
import pandas as pd
from pandas.api.types import CategoricalDtype
import matplotlib.pyplot as plt

diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()


cut_kategoriler = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories=cut_kategoriler, ordered=True))

#df["cut"].value_counts().plot.barh().set_title("Cut Değişkeninin Sınıf Frekansları")

#seaborn ile görselleştirme
sns.barplot(x = "cut",y = df.cut.index,data=df)
plt.show()



