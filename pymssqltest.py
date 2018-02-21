import  pymssql
from flask import Flask, request, jsonify
app = Flask(__name__)


server = '192.168.12.8'
user = 'sa'
password = 'Zabpod1932'
dbname = 'STORAGEandPICKING'

conn = pymssql.connect(server,user,password,dbname)
cursor = conn.cursor(as_dict=True)
cursor.execute('SELECT * FROM USERS')
rowlist = []
for row in cursor:
    rowlist.append({'Id':row['Id'],'UserName':row['UserName'], 'FirstName':row['FirstName'], 
        'LastName':row['LastName'], 'CodBranch':row['CodBranch'], 
        'Password':row['Password'], 'CreationDate':row['CreationDate']})

conn.close()
@app.route('/', methods=['GET'])
def home():
    return jsonify(rowlist)

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)