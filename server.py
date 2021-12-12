# Rest server API to access database.
# "Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs."
# Author: Isabell Doyle

# Command to run flask from terminal: 
# FLASK_APP=server.py FLASK_ENV=development flask run

# -*- coding: utf-8 -*-

from flask import Flask , url_for, request, redirect, abort, jsonify
from treeDao import treeDao

app = Flask(__name__, static_url_path='', static_folder='Static_pages')

@app.route('/')
def index():
    return "Tree Database"

# Gets all tree records.
@app.route('/trees')
def getAll():
    return jsonify(treeDao.getAll())

# Gets tree specified by id.
@app.route('/trees/<int:tree_id>')
def findById(tree_id):
    return jsonify(treeDao.findByID(tree_id))

# curl -X POST -d "{\"english_name\" : \"test\", \"irish_name\": \"test\", \"scientific_name\" : \"test\"}" -H Content-Type:application/json http://127.0.0.1:5000/trees
# Creates a new record.
@app.route('/trees', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    
    # tree id not included as it is set to auto-increment
    tree = {
        "english_name" : request.json["english_name"],
        "irish_name" : request.json["irish_name"],
        "scientific_name" : request.json["scientific_name"]
    }
    return jsonify(treeDao.create(tree))

# Updates record by id.
# curl -X PUT -d "{\"english_name\" : \"test\", \"irish_name\": \"test\", \"scientific_name\" : \"test\"}" -H Content-Type:application/json http://127.0.0.1:5000/trees/1001
@app.route('/trees/<int:tree_id>', methods = ['PUT'])
def update(tree_id):
    foundTree = treeDao.findByID(tree_id)
    # print(foundTree)
    if len(foundTree) == {}:
        return jsonify({}), 404
    currentTree = foundTree
    if 'english_name' in request.json:
        currentTree['english_name'] = request.json['english_name']
    if 'irish_name' in request.json:
        currentTree['irish_name'] = request.json['irish_name']
    if 'scientific_name' in request.json:
        currentTree['scientific_name'] = request.json['scientific_name']
    treeDao.update(currentTree)

    return jsonify(currentTree)

# Delete record by tree_id. 
# curl -X DELETE http://127.0.0.1:5000/trees/1003
@app.route('/trees/<int:tree_id>', methods = ['DELETE'])
def delete(tree_id):
    foundTree = treeDao.findByID(tree_id)
    
    # Returns error message if record not found.
    if foundTree == {}:
        return "Record not found.\n", 404
    
    # Delete.
    treeDao.delete(tree_id)
    return jsonify({"Done" : True})

if __name__ == "main":
    app.run(debug=True)
