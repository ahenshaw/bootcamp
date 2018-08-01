''' 
Read and analyze CSV file using numpy
'''
#%%
# third-party library
import numpy as np
import matplotlib.pyplot as plt

fn = 'c:/repos/bootcamp/data/CLEAN1A.csv'

data = np.loadtxt(fn, delimiter=',', skiprows=1)
#%%
print(data)

#%%
# get a convenient handle to the age column
age = data[:, 2]

#%% plot some data
plt.hist(age)
plt.show()

#%%
plt.hist(age, rwidth=0.9, normed=True)
plt.show()
