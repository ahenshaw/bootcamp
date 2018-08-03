# standard library
import sqlite3
# custom modules
from load_and_clean import load_raw, clean

DB_PATH = 'c:/repos/bootcamp/data/data.db'

def init_database():
    ''' Use Pandas dataframe to create the SQL table
        if it doesn't already exist
    '''

    # make a connection to our filesystem database
    db = sqlite3.connect(DB_PATH)

    try:
        db.execute('SELECT 1 FROM clean LIMIT 1')
    except sqlite3.OperationalError:
        df = clean(load_raw())
        df.to_sql(table_name, db)
    
    return db

