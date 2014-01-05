import MySQLdb as mdb
import sys

class Connection:
	def getConnection(self, dbConnection):
		self.dbConnection = dbConnection
#		print self.dbConnection
#		for key in self.dbConnection:
#			print key, 'corresponds to', self.dbConnection[key] 
#		print type(self.dbConnection)
		server =  self.dbConnection.get('server', "missing server name")
		userName =  self.dbConnection.get('userName', "missing userName")
		password = self.dbConnection.get('password', "missing passwrod")
		database =  self.dbConnection.get('database', "missing database Name")
		con = mdb.connect(server, userName, password, database)
#		con = "hello world from getConnection"
		return con

	def insertData(self, con, valuesAndTable):
		self.con = con
		self.valuesAndTable = valuesAndTable
		cur = self.con.cursor()
		value = self.valuesAndTable.get('value')
		unit = self.valuesAndTable.get('unit')
		tableName = self.valuesAndTable.get('tableName')
		sql = "insert into " + tableName + " ("+ tableName.upper() + ", UNIT) values ("+ str(value) + ",'" + unit + "')" 
		print sql
		error = cur.execute(sql)
		return error 
	
	def getVersion(self, con):
		cur = con.cursor()
		cur.execute("select version()")
		data = cur.fetchone()
		print data
		return data
	
	def disconnect(self, con):	
		con.close()
		
#except mdb.Error, e:
  
#    print "Error %d: %s" % (e.args[0],e.args[1])
#    sys.exit(1)
    
#finally:    
        
#    if con:    
#        con.close()
