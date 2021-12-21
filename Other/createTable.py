import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="native_trees"
)

myCursor = mydb.cursor()
sql="create table trees (tree_id int PRIMARY KEY AUTO_INCREMENT, english_name varchar(255), irish_name varchar(255), scientific_name varchar(255));)"
myCursor.execute(sql, multi=True)
print('sucess')