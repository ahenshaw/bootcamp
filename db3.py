''' db3 - Create SQL table (if needed)'''
# standard library
import sqlite3

# custom modules
from load_and_clean import load_raw, clean

DB_PATH = 'c:/repos/bootcamp/data/data.db'

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

cursor = db.cursor()
cursor.execute('SELECT * FROM clean')

for row in cursor.fetchall():
    print(row)