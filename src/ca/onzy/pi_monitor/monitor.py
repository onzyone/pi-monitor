import ast
import logging

from light import Light
from temperatureHumidity import DHT
#from rrd import RRD
from dictionary import Dictionary
import thermostat

class monitor():

	def __init__(self):
		self.logger = logging.getLogger("monitor")

	def getLight(self, verbose, myDict):
		Light().enable()
		lux = round((Light().getLux()),3)
		self.logger.info('lux: %s' %(lux))
		Light().disable()
		myDict = Dictionary().updateDict(myDict, 'light', lux)
		return myDict

	def getHumidity(self, verbose, myDict):
		humidity = DHT().getHumidity()
		self.logger.info('humidity: %s' %(humidity))
		myDict = Dictionary().updateDict(myDict, 'humidity',humidity)	
		return myDict

	def getTemperature(self, verbose, myDict):
		temperature = DHT().getTemperature()
		self.logger.info('temperature: %s' %(temperature))
		myDict = Dictionary().updateDict(myDict, 'temperature', temperature)
		return myDict

	def getThermostat(self, verbose, myDict):
		ther = thermostat.Thermostat()
		conn = ther.getConnection('192.168.1.128', 80) 
		currentTemp = ast.literal_eval(ther.getCurrentTemp(conn))
		currentTempC = round(((currentTemp.get('temp') - 32) / (9.0/5.0)),3)
		self.logger.info('thermostat: %s' %(currentTempC))
		myDict = Dictionary().updateDict(myDict, 'thermostat', currentTempC)
		return myDict