""""""
conn = sqlite3.connect('car.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_cars( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_cmake TEXT, \
        col_cyear TEXT, \
        col_mileage TEXT \
        )")
    conn.commit()
conn.close()



conn = sqlite3.connect('car.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_cmake, col_cyear, col_mileage) VALUES (?,?,?)", \
                ('Toyota', '2020', '31k'))
    cur.execute("INSERT INTO tbl_persons(col_cmake, col_cyear, col_mileage) VALUES (?,?,?)", \
                ('Audi', '2021', '47k'))
    cur.execute("INSERT INTO tbl_persons(col_cmake, col_cyear, col_mileage) VALUES (?,?,?)", \
                ('Nissan', '2022', '88k')) 

    conn.commit()
conn.close()


conn = sqlite3.connect('car.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_cMake,col_cYear,col_mileage FROM tbl_cars WHERE col_mileage = '88k'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "Car Make: {}\nCar Year: {}\nMileage {}".format(item[0],item[1],item[2])
    print(msg)

#fileList = ('information.docx', 'hello.txt', 'myImage.png', \
           # 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
