import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO db (name, pet) VALUES (?, ?)",
            ('Sasha', 'cat')
            )

cur.execute("INSERT INTO db (name, pet) VALUES (?, ?)",
            ('Masha', 'dog')
            )

cur.execute("INSERT INTO db (name, pet) VALUES (?, ?)",
            ('Bob', 'dog')
            )

cur.execute("INSERT INTO db (name, pet) VALUES (?, ?)",
            ('Vasya', 'pig')
            )

connection.commit()
connection.close()
