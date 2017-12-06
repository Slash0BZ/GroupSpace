import mysql.connector
import credentials
class Database:
	def __init__(self):
		self.connection = mysql.connector.connect(
                          user = credentials.getDatabaseUserName(),
                          password = credentials.getDatabaseUserPassword(),
                          host = credentials.getDatabaseHost(),
                          database = credentials.getDatabaseName())

	def __del__(self):
		self.connection.close()

	def queryByValue(self, table, EVs):
		queryString = "SELECT * FROM " + table + " WHERE "
		for (e, v) in EVs:
			queryString = queryString + e + "=" + "'" + v + "'" + " AND "
		if (queryString.endswith(" AND ")):
			queryString = queryString[:-5] 
		cursor = self.connection.cursor()
		cursor.execute(queryString)
		ret = []
		for c in cursor:
			ret.append(c)
		cursor.close()
		return ret

	def queryRoomBySpecs(self, noise, people, library):
		queryString = "SELECT * FROM room WHERE noise BETWEEN " + str(noise - 1) + " AND " + str(noise + 1) + " AND occupancy >= " + str(people) + " AND lid=" + str(library)
		cursor = self.connection.cursor()
		cursor.execute(queryString)
		ret = []
		for c in cursor:
			ret.append(c)
		cursor.close()
		return ret
	
	def queryRoomSpecs(self, rid):
		queryString = "SELECT * FROM room WHERE rid=" + str(rid)
		cursor = self.connection.cursor()
		cursor.execute(queryString)
		ret = []
		for c in cursor:
			ret.append(c)
		cursor.close()
		return ret

	def addTransaction(self, username, time, duration, rid):
		command = "INSERT INTO transaction (uid, username, time, duration, rid, roomname, people) VALUES (0, '" + username + "', '" + time + "', '" + duration + "', '" + rid + "', 'none', 'none')"
		cursor = self.connection.cursor()
		cursor.execute(command)
		self.connection.commit()

	def queryTransaction(self, username):
		queryString = "SELECT * FROM transaction WHERE username='" + username + "'"
		cursor = self.connection.cursor()
		cursor.execute(queryString)
		ret = []
		for c in cursor:
			ret.append(c)
		cursor.close()
		return ret

	def deleteTransaction(self, username, time):
		command = "DELETE FROM transaction WHERE username='" + str(username) + "' AND time='" + str(time) + "'"
		cursor = self.connection.cursor()
		cursor.execute(command)
		self.connection.commit()
