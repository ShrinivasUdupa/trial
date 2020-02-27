import mysql.connector
import csv

# Connecting Database
mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",db = "assessment4")
cursor = mydb.cursor()

# Inserting values into file
f = open("sale.csv")
c = f.read()
row_split = c.split(";")[0]
print(row_split)
for i in row_split.splitlines():
    rows = i.split(",")
    print("Aj")
    # print(i)

    # cursor.execute("insert into sale values (%s,%s,%s,%s)", i)
mydb.commit()