import seaborn as sns
import matplotlib.pyplot as plt


diamond = sns.load_dataset("diamonds")
df = diamond.copy()
print(df.head(10))

"""

sns.FacetGrid(df,hue = "cut",
              height=5,
              xlim=(0, 10000)).map(sns.kdeplot,"price",shade = True).add_legend()
plt.show()

"""

sns.catplot(x = "cut",y= "price",hue="color",kind="point",data=df)
plt.show()