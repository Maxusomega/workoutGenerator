import sqlite3

conn = sqlite3.connect('userEntry.db')

#create a cursor
c = conn.cursor()

#create a table

#
#c.execute("""CREATE TABLE "userInfo" (
#	"first_name"	TEXT,
#	"last_name"	TEXT,
#	"email"	TEXT UNIQUE,
#	"sport"	TEXT,
#	PRIMARY KEY("email")
#);""")

#c.execute("INSERT INTO  userInfo VALUES ('Matthew', 'Cole', 'swsmatthew@gmail.com','swim')")

c.execute("SELECT * FROM userInfo")
print(c.fetchall())

conn.commit()
conn.close()