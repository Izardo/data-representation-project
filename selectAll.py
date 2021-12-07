import mysql.connector

db = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="native_trees"
)

cursor = db.cursor()
sql="select * from trees"
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
 print(x)