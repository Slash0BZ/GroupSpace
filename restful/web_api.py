from flask import Flask, request, abort
import user

app = Flask(__name__)

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
		return "success", 202
	else:
		return "failure", 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
