"""
Alt küme üzerinde işlem yapmak
Alt kümeleri bağımsızlaştırmak

"""

import numpy as np
#Ana array bozuluyor....
a = np.random.randint(10,size=(5,5))
alt_a = a[0:3,0:2]
alt_a[0,0] = 999999
alt_a[1,1] = 888



#Ana array bozulmayacak

array = np.random.randint(10,size=(5,5))
print(array)
alt_array = array[0:3,0:2].copy()
print(alt_array)

alt_array[1,1] = 1999




















