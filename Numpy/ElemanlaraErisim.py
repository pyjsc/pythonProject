import numpy as np

"""
Tek boyutlu arraylerde Mantık listelerle aynıdır.
Çok boyutlu arraylarda satır ve sütun bilgisi girmemiz gerekir.
"""
array = np.random.randint(10,size=(3,3))
print(array)
erisim = array[(0,2)] #ilk değer satır son değer sütun.

"""
Zaten oluşturulmuş bir array e sonradan içerdeki tipten farklı olarak
bir değer eklemek istediğimiz zaman o değeri içerdeki tipe uyarlar .
Örneğin içerde sadece integerlardan oluşan bir değer olsun sonradan
biz bu array e float bir değer eklemek istediğimizde bu değeri integer a çevirir.
Örnek;
"""
array[(0,2)] = 3.4





