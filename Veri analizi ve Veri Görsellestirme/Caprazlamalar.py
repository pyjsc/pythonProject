import seaborn as sns
from pandas.api.types import CategoricalDtype
import matplotlib.pyplot as plt

diamonds = sns.load_dataset("diamonds")
df = diamonds.copy()

cut_kategoriler = ["Fair","Good","Very Good","Premium","Ideal"]
df.cut = df.cut.astype(CategoricalDtype(categories=cut_kategoriler,ordered=True))

#sns.catplot(x = "cut", y = "price",data=df)

sns.barplot(x = "cut",y = "price",hue = "color",data = df)
plt.show()

#grafik doğrulaması.
a = df.groupby(["cut","color"])["price"].mean() #önce "cut" a göre grupla sonra "color " a göre grupla ve bunun neticesinde "price "değişkenine göre ortalama işlemi yap.
print(a)



