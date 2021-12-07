# This program performs CRUD operations on a database.
import mysql.connector

# Create class to access database.
class treeDao:
    db = ""
    # Initiate database.
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost', 
            user = 'root', 
            password = '',
            database = 'native_irish_trees'
        )
        #print("Connection made!")

    def create(self, tree):
        cursor = self.db.cursor()
        sql = "insert into trees (english_name, irish_name, scientific_name) values (%s,%s,%s)"
        values = [
            tree['english_name'], 
            tree['irish_name'], 
            tree['scientific_name']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from trees"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from trees where tree_id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

    def update(self, values):
        cursor = self.db.cursor()
        sql = "update trees set english_name = %s, irish_name = %s, scientific_name = %s where tree_id = %s"
        cursor.execute(sql, values)
        self.db.commit()
        print("Update complete.")

    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from trees where tree_id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("Delete successful.")

treeDao = treeDao()