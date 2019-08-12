''' 
Read and filter CSV file using standard library
'''
# standard library
import csv
import sys
from pprint import pprint as pp

fn = 'data/CLEAN1A.csv'

# quick-and-dirty
data = list(csv.reader(open(fn, encoding="utf-8-sig")))
pp(data[:5])
sys.exit()

# better
with open(fn, encoding="utf-8-sig") as csvfile:
    data = list(csv.reader(csvfile))
pp(data[:5])
sys.exit()


# each record is a dictionary
with open(fn, encoding="utf-8-sig") as csvfile:
    data = list(csv.DictReader(csvfile))
pp(data[:5])
sys.exit()

#   why this is useful
#   assume large data set, 
#   just need records (or first record) 
#   that matches condition
with open(fn, encoding="utf-8-sig") as csvfile:
    for record in csv.reader(csvfile):
        if record[0].startswith('143'):
            print(record)
            break


# explain why "utf-8-sig" is needed
print(open(fn, 'rb').read(27))