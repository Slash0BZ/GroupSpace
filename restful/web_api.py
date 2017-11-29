from flask import Flask, request, abort
from flask.ext.cors import CORS
import user
import utils
import database
import json

app = Flask(__name__)
CORS(app, resources=r'/login/*', allow_headers='Content-Type')
CORS(app, resources=r'/getRoom/*', allow_headers='Content-Type')

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
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
