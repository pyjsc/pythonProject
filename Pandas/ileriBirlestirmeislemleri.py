import pandas as pd


#Birebir birleştirme


dataframe1 = pd.DataFrame({"calisanlar":["Ali","Mustafa","Ayşe","Fatma"],
                           "grup":["Muhasebe","Mühendislik","Mühendislik","İnsan Kaynakları"]})


dataframe2 = pd.DataFrame({"calisanlar":["Ali","Mustafa","Ayşe","Fatma"],
                           "ilk_giris":[2020,2009,2014,2019]})


#birlesme = pd.merge(dataframe1,dataframe2,on="calisanlar")


#coktan teke

dataframe3 = pd.merge(dataframe1,dataframe2)


dataframe4 = pd.DataFrame({"grup":["Muhasebe","Mühendislik","İnsan Kaynakları"],
                           "mudur":["Caner","Selma","Berkcan"]})


birlesme = pd.merge(dataframe3,dataframe4)


#çoktan çoka
dataframe5 = pd.DataFrame({"grup":["Muhasebe","Muhasebe",
                                   "Mühendislik","Mühendislik","İnsan Kaynakları",
                                   "İnsan Kaynakları"],
                           "Yetenekler":["Matematik","Excel","Kodlama","Linux","Excel","Yonetim"]})

birlesme2 = pd.merge(dataframe1,dataframe5)
print(birlesme2)













