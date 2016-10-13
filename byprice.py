###  -    https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04
from flask import Flask
from flask import request
from flask import json, jsonify
import pymysql as mdb
import sys

application = Flask(__name__)

@application.route("/")
#Controlador de ruta del index
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@application.route("/db")
#Drugs Database route controller
def database():
	# Initialize list of drugs
	medicamentosList = []
	# Initialize MySQL connector & cursor
	con = mdb.connect(user='testuser', passwd = 'test623', db = 'testdb', host = 'localhost', 
	    charset="utf8", use_unicode=True)
	cursor = con.cursor()
	# Fetch all saved values on the DB
	cursor.execute('SELECT * FROM item')
	medicamentoSet = cursor.fetchall()
	con.commit()
	cursor.close()
	con.close()

	# Create instances for filling up the list
	# And Append to the list of Drugs
	for med in medicamentoSet:
		medicamentosList.append(med)
	# Return jsonified elements 
	return jsonify(medicamentosList)

@application.route("/db/<string:search>")
#Drugs Database route controller
def dbSearch(search):
	# Initialize MySQL connector & cursor
	con = mdb.connect(user='testuser', passwd = 'test623', db = 'testdb', host = 'localhost', 
	    charset="utf8", use_unicode=True)
	cursor = con.cursor()
	# Fetch all saved values on the DB that are into the 
	cursor.execute("SELECT * FROM item WHERE (NOMBRE LIKE %s )",
	                ("%" + search + "%"))
	medicamentoSet = cursor.fetchall()
	con.commit()
	cursor.close()
	con.close()
	# Initialize list of drugs
	medicamentosList = []
	# Create instances for filling up the list
	# And Append to the list of Drugs
	for med in medicamentoSet:
		medicamentosList.append(med)
	# Return jsonified elements 
	return jsonify(medicamentosList)

# You can convert to different data with <converter:variable_name>
@application.route("/user/<username>")
#User route controller
def user(username):
    return "<h1 style='color:blue'> User is: %s </h1>" %username

# HTTP Methods
#@application.route("/login", methods=['GET', 'POST'])
#Login route controller
#def login():
#	if request.method == 'POST':
#		return "<h1 style='color:blue'> POST method implemented </h1>"
#	else:
#		return "<h1 style='color:blue'> Something's wrong </h1>"


if __name__ == '__main__':
	application.run(host='0.0.0.0')