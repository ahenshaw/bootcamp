''' 
Read and analyze CSV file using Pandas
'''
#%%
# third-party library
import pandas as pd
import matplotlib.pyplot as plt

fn = '/repos/bootcamp/data/CLEAN1A.csv'

data = pd.read_csv(fn)
#%%
print(data)
print(data.describe())

#%% plot some data
data.AGE.plot(kind='hist')
plt.show()

#%%
data.AGE.plot(kind='hist', rwidth=0.9, normed=True)
plt.show()


