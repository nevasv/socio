import sqlite3
from dataclasses import dataclass
db = sqlite3.connect('db.db')
cur = db.cursor()
# cur.execute(""" CREATE TABLE PERSON
# (person_id INTEGER PRIMARY KEY NOT NULL,
# email TEXT NOT NULL,
# login TEXT NOT NULL,
# UNIQUE (email, login)
# )""")
# db.commit()
cur.execute("""INSERT INTO PERSON (email, login) VALUES
(
'nevasv@yandex.ru',
'nevasv'
)
""")
db.commit()
db.close()


