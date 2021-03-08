"""
Koşullu eleman işlemleri
"""

import numpy as np

v = np.array([1,2,3,4,5])

kosul = v < 5 #Şartı sağlayan tüm değerleri True , Sağlamayanları False olarak işaretledi.

#fancy ile şartı sağlayanları yakalama(görme,alma)

yakala = v[v<5]#şartı sağlayanları çeker.

uygula = v ** 2 #Uyguladığımız matematiksel işlemi tüm elemanlara uygular
print(uygula)