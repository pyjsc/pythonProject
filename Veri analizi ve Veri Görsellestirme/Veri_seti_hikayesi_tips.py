import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")
df = tips.copy()

print(df.head(10))


