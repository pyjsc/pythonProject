import pandas as pd

#csv okuma
icerik = pd.read_csv("reading_data\ornekcsv.csv",sep = ";")

#txt okuma
icerik2 = pd.read_csv("reading_data\duz_metin.txt")

#excel okuma
icerik3 = pd.read_excel("reading_data\ornekx.xlsx")
icerik3.columns = ["A","B","C"] #değişkenlerin ismini değiştirdik.

