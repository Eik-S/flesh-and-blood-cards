import psycopg2
from tables import *

database_name = 'fabcards'

#establishing the connection to postgres
conn = psycopg2.connect(
    database=database_name, user='postgres', password='password', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

### Get current database names
cursor.execute("SELECT datname FROM pg_database;")

list_database = cursor.fetchall()

### Create database if it doesn't exist already
if (database_name,) not in list_database:
    print("'{}' database does not exist, creating it.".format(database_name))
    cursor.execute('''CREATE database fabcards''')
    print("'{}' database created successfully...........".format(database_name))

### Drop existing tables, recreate them, and then fill them with data
drop_tables(conn)
print()
create_tables(conn)
print()
generate_table_data(conn)

conn.close()

print('Done creating tables from CSVs!')