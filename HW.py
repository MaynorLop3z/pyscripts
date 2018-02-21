import  pyodbc
from flask import Flask, jsonify, request

app = Flask(__name__)

cnxn = pyodbc.connect("Driver={ODBC Driver 11 for SQL Server};"
                      "Server=192.168.12.8;"
                      "Database=STORAGEandPICKING;"
                      ";UID=sa;PWD=Zabpod1932")

rowlist = []
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM USERS')
rows = cursor.fetchall()
for row in rows:
    t = ({'Id':row.Id,'UserName':row.UserName, 'FirstName':row.FirstName, 
        'LastName':row.LastName, 'CodBranch':row.CodBranch, 
        'Password':row.Password, 'CreationDate':row.CreationDate})
    rowlist.append(t)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/test')
def test():
    return '<h1>this is a test</h1>'


@app.route('/profile/<user>')
def profile(user):
    return "Hi %s" % user

@app.route('/post/<int:id>')
def post(id):
    return "Hi, Post ID is %s" % id

@app.route('/getAllUsers', methods=['GET'])
def getAllUsers():
    return jsonify(rowlist)

@app.route('/getOneUser/<user>', methods=['GET'])
def getOneUser(user):
    user = [row for row in rowlist if row['UserName'] == user]
    return jsonify(user)

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)