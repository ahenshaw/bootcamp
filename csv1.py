#%%
# standard library
import csv
from pprint import pprint as pp

fn = 'c:/repos/bootcamp/data/CLEAN1A.csv'

#%% quick-and-dirty
data = list(csv.reader(open(fn, newline='')))
pp(data[:5])

#%% better
with open(fn, newline='') as csvfile:
    data = list(csv.reader(csvfile))
pp(data[:5])

with open(fn, newline='') as csvfile:
    data = list(csv.DictReader(csvfile))
pp(data[:5])
