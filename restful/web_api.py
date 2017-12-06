from flask import Flask, request, abort
from flask.ext.cors import CORS
import user
import utils
import database
import json

app = Flask(__name__)
CORS(app, resources=r'/login/*', allow_headers='Content-Type')
CORS(app, resources=r'/getRoom/*', allow_headers='Content-Type')
CORS(app, resources=r'/queryRoom/*', allow_headers='Content-Type')
CORS(app, resources=r'/addTransaction/*', allow_headers='Content-Type')
CORS(app, resources=r'/queryTransaction/*', allow_headers='Content-Type')
CORS(app, resources=r'/deleteTransaction/*', allow_headers='Content-Type')

@app.route('/')
def handle_root():
	return "<h1>GroupSpace<h2>"

@app.route('/login', methods = ['GET', 'POST'])
def handle_login():
	username = request.args.get("username")
	password = request.args.get("password")
	curUser = user.User(username, password)	
	status = curUser.login()
	if (status):
		return "success"
	else:
		return "failure"

@app.route('/getRoom', methods = ['GET', 'POST'])
def handle_getRoom():
	noise = request.args.get("noise")
	people = request.args.get("people")
	library = request.args.get("library")
	noise = int(noise)
	poeple = int(people)
	library = int(library)
	db = database.Database()
	result = db.queryRoomBySpecs(noise, people, library)
	output = []
	for entry in result:
		cur = {}
		cur["rid"] = entry[0]
		cur["name"] = entry[1]
		cur["position"] = entry[7]
		output.append(cur)
	return json.dumps(output)

@app.route('/queryRoom', methods = ['GET', 'POST'])
def handle_queryRoom():
	rid = request.args.get("rid")
	db = database.Database()
	result = db.queryRoomSpecs(rid)
	output = {}
	output["rid"] = result[0][0]
	output["roomname"] = result[0][1]
	output["occupancy"] = result[0][3]
	output["equip"] = result[0][4]
	output["noise"] = result[0][5]
	return json.dumps(output)

@app.route('/addTransaction', methods = ['GET', 'POST'])
def handle_addTransaction():
	username = request.args.get("username")
	time = request.args.get("time")
	duration = request.args.get("duration")
	rid = request.args.get("rid")
	db = database.Database()
	db.addTransaction(username, time, duration, rid)
	return "Success"

@app.route('/queryTransaction', methods = ['GET', 'POST'])
def handle_queryTransaction():
	username = request.args.get("username")
	db = database.Database()
	result = db.queryTransaction(username)
	output = []
	for entry in result:
		cur = {}
		cur["time"] = entry[2]
		cur["duration"] = entry[3]
		cur["rid"] = entry[4]
		output.append(cur)
	return json.dumps(output)

@app.route('/deleteTransaction', methods = ['GET', 'POST'])
def handle_deletion():
	username = request.args.get("username")
	time = request.args.get("time")
	db = database.Database()
	db.deleteTransaction(username, time)
	return "Success"
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
