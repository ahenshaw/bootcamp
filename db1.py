''' db1 - Demonstrate importing our own module '''
import matplotlib.pyplot as plt
# custom modules
from load_and_clean import load_raw, clean

df = clean(load_raw())
print(df.describe())
print(df.head())
df.AGE.plot(kind='hist')
plt.show()