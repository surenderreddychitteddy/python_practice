'''This script can be used to check if a database already exists with given name, if yes it will connect to the existing database, 
else it will create a new database.'''

import pymysql.cursors

connection = ''

try:
	connection = pymysql.connect(host='localhost',user='username',password='password',database='database_name')
except pymysql.err.InternalError as e:
	if "Unknown database" in str(e):
		connection = pymysql.connect(host='localhost',user='username',password='password')
		cursor = connection.cursor()
		cursor.execute("CREATE DATABASE database_name")
	else:
		error = str(e)	
except pymysql.err.OperationalError as e:
	error = str(e)
except TypeError as e:
	error = str(e)
