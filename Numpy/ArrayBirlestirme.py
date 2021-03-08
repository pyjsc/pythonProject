"""
Array birleştirme (Concatenation)


"""

import numpy as np

#TEK BOYUTLU BİRLEŞTİRME
x = np.array([1,2,3])
y = np.array([4,5,6])

xy_birlesim = np.concatenate([x,y])

z = np.array([7,8,9])

xyz_birlesim = np.concatenate([x,y,z])

#İKİ BOYUTLU BİRLEŞTİRME

a = np.array([[1,2,3],
              [4,5,6]])

abirlesim = np.concatenate([a,a])


eksenbirlesim = np.concatenate([a,a], axis=0)#axix eksen belirtmek için kullanılır .
#axis = 0 olduğunda satırları,
#axis = 1 olduğunda sütunları ifade eder.
print(eksenbirlesim)



