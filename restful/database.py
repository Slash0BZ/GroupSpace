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

	def queryRoomBySpecs(self, equip, noise, people):
		queryString = "SELECT * FROM room WHERE equipments LIKE '%equip%' AND noise BETWEEN " + str(noise - 2) + " AND " + str(noise + 2) + " AND occupancy >= " + people
		cursor = self.connection.cursor()
		cursor.execute(queryString)
		ret = []
		for c in cursor:
			ret.append(c)
		cursor.close()
		return ret
