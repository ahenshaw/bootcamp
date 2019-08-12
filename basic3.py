# importing modules
#-----------------------------------------
# this is okay
import math
d = 90
a = math.sin(math.radians(d))
print(f'sin of {d:2.0f} degrees = {a}')

#-----------------------------------------
# this is okay
from math import cos, radians
d = 0
a = cos(radians(d))
print(f'cos of {d:2.0f} degrees = {a}')

#-----------------------------------------
# very rarely should you do this
from math import *
a = tan(tanh(cos(acos(sin(pi)))))
print('a =', a)

#-----------------------------------------
# this is common practice
# import numpy as np
# import pandas as pd

# a = np.array([1, 2, 3])
# df = pd.DataFrame()
