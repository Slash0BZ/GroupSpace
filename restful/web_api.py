from flask import Flask, request, abort
from flask.ext.cors import CORS
import user
import utils

app = Flask(__name__)
CORS(app, resources=r'/login/*', allow_headers='Content-Type')

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
	equipments = request.args.get("equipments")
	noise = request.args.get("noise")
	people = request.args.get("people")
	if "monitor" in equipments:
		equipments = "0"
	if "whiteboard" in equipments:
		equipments = "1"
	noise = int(noise)
	poeple = int(people)
	db = database.Database()
	result = db.queryRoomBySpecs(equipments, noise, people)
	print result
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
