import pandas as pd
import seaborn as sns

df = pd.DataFrame({"Gruplar":["A","B","C","A","B","C"],
                   "Veri":[10,11,52,23,43,55]},columns=["Gruplar","Veri"])
print(df)

#Ortalamasını aldık
grup = df.groupby("Gruplar").mean()


df2 = sns.load_dataset("planets")

grup2 = df2.groupby("method")["orbital_period"].describe()
print(grup2)