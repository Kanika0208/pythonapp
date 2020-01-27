from flask import (
Flask,
request,
json,
jsonify,
)
import mysql.connector
import mysql
import os
# Create the application instance
app = Flask(__name__)
@app.route('/')
def api_root():
	return 'Welcome'
	#Module to read all the records from table"********************************************
@app.route('/read', methods=['GET', 'POST'])
def read_table():
	mydb = mysql.connector.connect(
	host= os.environ['DB_HOSTNAME'], 
	user= os.environ['DB_USERNAME'], 
	passwd= os.environ['DB_PASSWORD'],
	database= os.environ['DB_NAME'] 
	)
	cur = mydb.cursor()
	output={}
	tmp=[]
	if request.method == 'GET':
		sql1="""SELECT * from employee"""
		cur.execute(sql1)
		data=cur.fetchall()
		mydb.close()
		for i in data:
			tmp.append({'id': str(i[0]),'name': str(i[1])})
		output=tmp
		return jsonify(output)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)