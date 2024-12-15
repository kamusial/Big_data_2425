import sqlite3

conn = sqlite3.connect('dane\\test.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)
            ''')

c.execute('''
        INSERT INTO users (name, age)
        VALUES ('Kamil', 36)
            ''')

c.execute('''
        INSERT INTO users (name, age)
        VALUES ('Marta', '26')
        ''')

c.execute('DELETE FROM users WHERE id = 1')

conn.commit()

c.execute('SELECT * FROM users')
print(c.fetchall())

conn.close()