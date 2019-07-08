"""Connection, cursor are the variables returned from connecting_to_database.py file.
table_creation() is used to check if there is a table already created with given name, if not created it will create a new table"""

import connecting_to_database # importing connecting_to_database.py


def table_creation(connection,cursor,req_table):
	try:
		cursor.execute('use database_name')
		cursor.execute('show tables')
		table_list=[each[0] for each in cursor]
		for each_table in req_table.keys():
			if each_table in table_list:
				print(each_table+' table already exist')
				continue
			else:
				cursor.execute(req_table[each_table])
				table_list.append(each_table)
				print(each_table+' table created successfully')
		return table_list		
	
	except Exception as e:
		print(str(e))
		return ""
    
    
def insert_values(connection,cursor,table_obj):
	try:
		for each_table in table_obj:
			sql = "SELECT * FROM %s" % (each_table)
			cursor.execute(sql)
			cursor.fetchall()
			count = cursor.rowcount
			if count==0:
				if each_table=='customers':
					sql = "INSERT INTO customers (cust_type) VALUES (%s)"
					val = [('AMAZON',),('AZURE',),('GOOGLE',)]
					cursor.executemany(sql,val)
					connection.commit()
					print(each_table+' table Data inserted successfully')
				elif each_table=='users':
					sql = "INSERT INTO users (username,password,firstname,lastname,email_id) VALUES (%s,%s,%s,%s,%s)"
					val = [('admin',),('surender',),('reddy',)]
					cursor.executemany(sql,val)
					connection.commit()
					print(each_table+' table Data inserted successfully')
				else:
					continue
			else:
				print (each_table+' table values already exists')
				continue
		return "success"	
		
	except Exception as e:
		print(str(e))
		return ""
    
 
    
mydb = connecting_to_database.connection 

req_table={'customers':'CREATE TABLE customers (cust_id INT AUTO_INCREMENT PRIMARY KEY,cust_type VARCHAR(100) NOT NULL)',
'users':'CREATE TABLE users (username VARCHAR(50) NOT NULL PRIMARY KEY,password VARCHAR(50),firstname VARCHAR(50),lastname VARCHAR(50),email_id VARCHAR(100))'}

if not mydb:
  print('DATABASE_CONNECTION_ERROR : '+db_connection.error)
else:
  mycursor = mydb.cursor()
	table_creation_output=table_creation(mydb,mycursor,req_table)
  
	if not table_creation_output:
		db_close(mydb,mycursor)
		print('Error while table creation')
	else:
		table_insertion_output=insert_values(mydb,mycursor,table_creation_output)
    
		if not table_insertion_output:
			db_close(mydb,mycursor)
			print('Error while value insertion in tables')
		else:
		db_close(mydb,mycursor)
