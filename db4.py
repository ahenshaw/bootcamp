# standard library
import sqlite3

# third-party libraries
import pandas as pd

'''db4 - Table to dataframe'''
# custom modules
from load_and_clean import load_raw, clean

DB_PATH = 'data/data.db'

SQL_AGE = '''
    SELECT AGE as age, COUNT(*) as count 
    FROM clean 
    GROUP BY AGE
'''

def init_database(db):
    ''' Use Pandas dataframe to create the SQL table
        if it doesn't already exist
    '''
    try:
        db.execute('SELECT 1 FROM clean LIMIT 1')
    except sqlite3.OperationalError:
        df = clean(load_raw())
        df.to_sql(table_name, db)

# make a connection to our filesystem database
db = sqlite3.connect(DB_PATH)
init_database(db)

# SQL query turned into a data frame
age_table = pd.read_sql_query(SQL_AGE, db)
with pd.option_context('display.max_rows', 10):
    print(age_table)



