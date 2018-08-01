''' 
Read CSV file and return dataframe using Pandas 
'''
# third-party library
import pandas as pd

# custom libraries
from impute import impute

fn = 'c:/repos/bootcamp/data/NOTCLEAN1A.csv'

def load_raw():
    return pd.read_csv(fn)


def clean(df):
    df = df.drop(['TRADES'], axis=1)
    df = df.set_index('MATCHKEY')
    df = impute(df)

    # update column types
    df = df.astype(int)

    return df

def load():
    return clean(load_raw())

if __name__ == '__main__':
    data = load_raw()
    print(data.describe())

    cleaned = clean(data)
    print(cleaned.describe())
    print(cleaned.head())

    print(load())
