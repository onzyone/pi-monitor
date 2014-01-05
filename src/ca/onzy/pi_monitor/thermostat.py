import httplib, string, json

class Thermostat(object):

	def getConnection(self, base, port):
		conn = httplib.HTTPConnection(base, port, timeout=60)
		return conn

	def readWebService(self, conn, url):
		conn.request('GET', url, None)
		data = conn.getresponce().read()
		return data	

	def getCurrentTemp(self, conn):
		#conn = httplib.HTTPConnection(base, port, timeout=60)
		url = '/tstat/temp'
		conn.request('GET', url, None)
		data = conn.getresponse().read()	
		return data
