''' 
    Flask app to perform CRUD operations on a Native Irish Tree database.
    Isabella Doyle
'''

from flask import Flask , url_for, request, redirect, abort, jsonify, render_template, session, g
from flask_cors import CORS
from treeDao import treeDao

app = Flask(__name__, static_url_path='', static_folder='Static', template_folder='templates')
CORS(app)

# Cookie signature.
app.secret_key = 'secretkey'

# User object.
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password 

    def __repr__(self):
        return f'<User: {self.username}>'

# Create user objects.
users = []
users.append(User(id=1, username='Andrew', password='password'))
users.append(User(id=2, username='Izzy', password='password'))

# Store current user.
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

# Route to login page.
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        # Log out any user.
        session.pop('user_id', None)

        # Get user data from form.
        username = request.form['uname']
        password = request.form['psw']

        # Authenticate username & password.
        try:
            user = [x for x in users if x.username == username][0]
            if user and user.password == password:
                session['user_id'] = user.id
                return redirect(url_for('profile'))
        except:
            return render_template('/login.html')

    return render_template('/login.html')

# Route to logged in user's profile.
@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('/profile.html')

# Routes to CRUD operations.
@app.route('/')
def main():
    return render_template('/login.html')

# Route to static page with tree database.
@app.route('/index')
def index():

    # Checks if user is authenticated.
    if not g.user:
        return redirect(url_for('login'))
    else:
        return render_template('/index.html')

# Gets all tree records.
@app.route('/trees')
def getAll():
    return jsonify(treeDao.getAll())

# Gets tree specified by id.
@app.route('/trees/<int:tree_id>')
def findById(tree_id):
    return jsonify(treeDao.findByID(tree_id))

# Creates a new record.
# curl -X POST -d "{\"english_name\" : \"test\", \"irish_name\": \"test\", \"scientific_name\" : \"test\"}" -H Content-Type:application/json http://127.0.0.1:5000/trees
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

'''

References:

    The authentication code was adapted from: https://www.youtube.com/watch?v=2Zz97NVbH0U
    
'''