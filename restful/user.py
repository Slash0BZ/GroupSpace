import database
class User:
	def __init__(self, u, p):
		self.username = u
		self.password = p
		self.login_status = False

	def login(self):
		db = database.Database()
		result = db.queryByValue("user", [("username", self.username),
                                          ("password", self.password)])
		if (len(result) == 1):
			self.login_status = True
			return True
		return False
