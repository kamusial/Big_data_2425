import sqlite3

conn = sqlite3.connect('dane\\results.db')
c = conn.cursor()

c.execute('SELECT name FROM sqlite_master WHERE type="table";')
tables = c.fetchall()

for table in tables:
    print(table[0])

conn.close()

