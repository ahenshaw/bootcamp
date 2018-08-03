''' 
Read CSV file and return dataframe using Pandas 
'''
# third-party library
import pandas as pd

# custom libraries
from impute import impute

fn = 'c:/repos/bootcamp/data/NOTCLEAN1A.csv'

def load_raw():
    print('Reading from "{}"'.format(fn))
    return pd.read_csv(fn)


def clean(df):
    df = df.drop(['TRADES'], axis=1)
    df = df.set_index('MATCHKEY')
    df = impute(df)

    # update column types
    df = df.astype(int)

    return df


if __name__ == '__main__':
    data = load_raw()
    print('Raw Data: Summary')
    print(data.describe())
    print('\nRaw Data: Head')
    print(data.head())

    cleaned = clean(data)
    print('\n\nCleaned Data: Summary')
    print(cleaned.describe())
    print('\nCleaned Data: Head')
    print(cleaned.head())

