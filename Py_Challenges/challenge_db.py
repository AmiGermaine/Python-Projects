import sqlite3

conn = sqlite3.connect('roster_db')

c = conn.cursor()

#c.execute(""" CREATE TABLE Roster(
#          Name TEXT,
#          Species TEXT,
#          IQ INTEGER
#    )""")

c.execute("INSERT INTO Roster VALUES ('Jean-Baptiste Zorg', 'Human', 122)")

all_Roster = (
    ('Korben Dallas', 'Human', 100)
    ('Aknot', 'Mangalore', -5)
)

c.executemany("INSERT INTO Roster VALUES (?, ?, ?)", all_Roster)

c.execute("SELECT * FROM Roster")
print(c.fetchall)

conn.commit()
conn.close()
