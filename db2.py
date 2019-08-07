''' db2 - Create SQL table'''

# standard library
import sqlite3

# custom modules
from load_and_clean import load_raw, clean

DB_PATH = 'data/data.db'
# mode    = 'fail'
mode    = 'replace'

# make a connection to our filesystem database
db = sqlite3.connect(DB_PATH)

# use Pandas dataframe to create an SQL table
df = clean(load_raw())
df.to_sql('clean', db, if_exists=mode)

cursor = db.cursor()
cursor.execute('SELECT * FROM clean')

for row in cursor.fetchall():
    print(row)