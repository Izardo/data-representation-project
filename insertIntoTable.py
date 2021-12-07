import mysql.connector

db = mysql.connector.connect(
 host = "localhost",
 user = "root",
 password = "",
 database = "native_trees"
)

cursor = db.cursor()
sql = "insert into trees (english_name, irish_name, scientific_name) values (%s,%s,%s)"
values = ("Alder", "Fearnóg", "Alnus glutinosa")
cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)