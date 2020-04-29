import pymysql
import os
#from app import app
#from config import mysql
from flask import jsonify
from flask import flash, request
from flask import Flask
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
		

app = Flask(__name__)
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'restpython'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/user', methods=['GET','POST'])
def add_emp():
	
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_age =_json['age']
		_department = _json['department']
		_subject = _json['subject']
        	print("before working")
		if _id and _name and _age and _department and _subject and request.method == 'POST':			
			sqlQuery = "INSERT INTO user(id,name,age,department,subject) VALUES(%s, %s, %s, %s, %s)"
			bindData = (_id,_name,_age,_department,_subject)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('User added successfully!')
			respone.status_code = 200
			return respone
		else:
			return 'ok'
			



	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



'''
@app.route('/user', methods=['GET'])
def emp():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, age, department, subject FROM user")
		empRows = cursor.fetchall()
		respone = jsonify(empRows)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
'''
		
@app.route('/user/<int:id>', methods=['GET'])
def emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, name, age, department, subject FROM user WHERE id =%s", (id,))
		empRow = cursor.fetchone()
		respone = jsonify(empRow)
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_emp(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM user WHERE id =%s", (id,))
		conn.commit()
		respone = jsonify('User deleted successfully!')
		respone.status_code = 200
		return respone
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/user', methods=['PUT'])
def update_emp():
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_age = _json['age']
		_department = _json['department']
		_subject = _json['subject']

		if _id and _name and _age and _department and _subject and request.method == 'PUT':
			sqlQuery = "UPDATE user SET name=%s, age=%s, department=%s, subject=%s WHERE id=%s"
			bindData = (_name, _age, _department, _subject, _id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sqlQuery, bindData)
			conn.commit()
			respone = jsonify('User updated successfully!')
			respone.status_code = 200
			return respone
		else:
			return not_found()	
	except Exception as e:
	 	print(e)
	finally:
	 	cursor.close() 
	 	conn.close()

		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":

	port = int(os.environ.get("PORT", 8080	))
    	app.run(debug=True,host='0.0.0.0',port=port)
