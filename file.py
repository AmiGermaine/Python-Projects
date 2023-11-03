import sqlite3

conn = sqlite3.connect('file.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT)")
    conn.commit()

# tuple of files
fileList = ('information.docx', 'hello.txt', 'myImage.png', \
           'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each object in the tuple to find the names that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_file (col_fname) VALUES (?)", (x,))
            print(x)
conn.close()
