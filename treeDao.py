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
            database = 'native_trees'
        )
        #print("Connection made!")

    def create(self, tree):
        cursor = self.db.cursor()
        sql = "insert into trees (tree_id, english_name, irish_name, scientific_name) values (%s,%s,%s,%s)"
        values = [
            tree['tree_id'], 
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
        sql = "select * from trees where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result

    def update(self, values):
        cursor = self.db.cursor()
        sql = "update trees set english_name = %s, irish_name = %s, scientific_name = %s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

treeDao = treeDao()