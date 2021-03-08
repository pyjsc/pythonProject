"""
Veri setleri üzerinde bazı satır ve sütun işlemleri yaparak veri setini amaca uygun bir şekle getirmek için kullanılan yapılardır
groupby ın çok boyutlu versiyonu olarak düşünülebilir.
"""
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic")
#ilkel pivotlama -- -groupby ile table
grup1 = titanic.groupby("sex")["survived"].mean()

grup2 = titanic.groupby(["sex","class"])["survived"].aggregate("mean").unstack()


#pivot ile table
grup3 = titanic.pivot_table("survived",index="sex",columns="class")

#değişken dönüşümleri
age = pd.cut(titanic["age"],[0,18,90])
donusum = titanic.pivot_table("survived",["sex",age], "class")
print(donusum)
