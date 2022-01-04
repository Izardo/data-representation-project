# Program performs CRUD operations on a database.
# Author: Isabella Doyle

import mysql.connector
import dbconfig as cfg

# Class to access database.
class treeDao:
    db = ""
    
    # Initiate database.
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'], 
            user = cfg.mysql['username'], 
            password = cfg.mysql['password'],
            database = cfg.mysql['database']
        )
        #print("Connection made!")

    # Create new record in database. 
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

    # Retrieve all records from database.
    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from trees"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    # Find record with specified id. 
    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from trees where tree_id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    # Update a record specified by id. 
    def update(self, tree): 
        cursor = self.db.cursor()
        sql = "update trees set english_name = %s, irish_name = %s, scientific_name = %s where tree_id = %s"
        values = [
            tree['english_name'],
            tree['irish_name'],
            tree['scientific_name'],
            tree['tree_id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return tree

    # Delete record specified by id. 
    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from trees where tree_id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("Delete successful.")
        # Add in code to see if id exists

    # Convert record from tuple to dict object. 
    def convertToDict(self, result):
        colNames = ['tree_id', 'english_name', 'irish_name', 'scientific_name']
        tree = {}

        if result:
            for i, colName in enumerate(colNames):
                value = result[i]
                tree[colName] = value
        return tree
         
treeDao = treeDao()