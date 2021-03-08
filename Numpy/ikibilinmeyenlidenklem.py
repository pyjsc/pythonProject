import numpy as np

"""
ilk denklem : 5x + y = 12
ikinci denklem : x + 3y = 10
"""



v = np.array([[5,1], [1,3]]) #ilk index ilk denklemin katsayıları , ikinci index ise ikinci denklemin katsayılarını ifade ediyor.
v2 = np.array([12,10]) #ilk değer ilk denklemin sonucunu , ikinci değer ise ikinci değerin sonucunu ifade ediyor.

x = np.linalg.solve(v, v2)
print(x)
