'''db5 - Focusing on the analytics'''

# third-party libraries
import pandas as pd
import database

SQL_AGE = '''
    SELECT AGE as age, COUNT(*) as count 
    FROM clean 
    GROUP BY AGE'''

SQL_ALL = 'SELECT * FROM clean'

db = database.init_database()

# SQL query turned into a dataframe
age_table = pd.read_sql_query(SQL_AGE, db)
print(age_table)

# SQL query loading all data into dataframe
df = pd.read_sql_query(SQL_ALL, db, index_col='MATCHKEY')
print(df.describe())