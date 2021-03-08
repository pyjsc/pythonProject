import seaborn as sns
planets = sns.load_dataset("planets")
df = planets.copy()

#Sürekli değişkenleri çekmek
df_num = df.select_dtypes(include=["float64","int64"])

#Bütün elemanların betimsel istatistiklerine erişmek
print(df_num.describe())

#Sadece belirli bir değişkenin betimsel istatistiklerine erişmek
sorgu = df_num["distance"].describe()
print(sorgu)

