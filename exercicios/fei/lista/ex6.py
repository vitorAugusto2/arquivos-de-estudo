"""
As temperaturas de uma cidade foram armazenadas na lista temperaturas =
[-10, -8, 0, 1, 2, 5, -2, -4 ]. Faça um programa que imprime a menor e a maior
temperatura, assim como a média.
"""

import numpy as np

temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4 ]

temp = np.array(temperaturas)
print(np.min(temp))
print(np.max(temp))
print(np.mean(temp))

#

print(min(temperaturas))
print(max(temperaturas))
print(sum(temperaturas)/len(temperaturas))