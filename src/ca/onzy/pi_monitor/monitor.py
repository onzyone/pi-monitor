import argparse, logging, os, json, ast

from light import Light
from temperatureHumidity import DHT
from rrd import RRD
from dictionary import Dictionary
import thermostat

def buildParser():
	parser = argparse.ArgumentParser(description='This is monitroing script for Temp, Light and Humidty')
	paa = parser.add_argument
        paa('-l', '--light', dest='light', action='store_true', 
		help='get light value in Lux')
        paa('-u', '--humidity', dest='humidity', action='store_true', 
		help='get humidity in %')
        paa('-t', '--temperature', dest='temperature', action='store_true', 
		help='get temperature in oC')
        paa('--thermostat', dest='thermostat', action='store_true', 
		help='get json back from thermostat ct50')
	paa('-a', '--all', dest='all', action='store_true', 
		help='get all of the above')
	paa('-v', '--verbose', dest='verbose', action='store_true', 
		help='will print values')
	paa('--version', action='version', version='%(prog)s 2.0')

	args = parser.parse_args()

	return args 

def startLogger(loggerName, loggerFolder):
	logger = logging.getLogger(loggerName)
	handler = logging.FileHandler(os.path.join(loggerFolder+'/'+loggerName+'.log'),'w')
	formatter = logging.Formatter('%(asctime)s -- %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel(logging.INFO)
	return logger

def getLight(logger, verbose, myDict):
	Light().enable()
        lux = round((Light().getLux()),3)
        logger.info('lux: %s' %(lux))
        Light().disable()
	myDict = Dictionary().updateDict(myDict, 'light', lux)
	return myDict

def getHumidity(logger, verbose, myDict):
	humidity = DHT().getHumidity()
        logger.info('humidity: %s' %(humidity))
	myDict = Dictionary().updateDict(myDict, 'humidity',humidity)	
	return myDict

def getTemperature(logger, verbose, myDict):
	temperature = DHT().getTemperature()
        logger.info('temperature: %s' %(temperature))
	myDict = Dictionary().updateDict(myDict, 'temperature', temperature)
	return myDict

def getThermostat(logger, verbose, myDict):
	ther = thermostat.Thermostat()
	conn = ther.getConnection('192.168.1.128', 80) 
	currentTemp = ast.literal_eval(ther.getCurrentTemp(conn))
	currentTempC = round(((currentTemp.get('temp') - 32) / (9.0/5.0)),3)
	logger.info('thermostat: %s' %(currentTempC))
	myDict = Dictionary().updateDict(myDict, 'thermostat', currentTempC)
	return myDict

def main():
	
	logger = startLogger('monitor', '/opt/projects/monitor/logs')
	args = buildParser()
	verbose = False
	
	myDict = Dictionary().newDict()

	if args.verbose:
		verbose = True
	if args.light:
		logger.info('light')
		myDict = getLight(logger, verbose, myDict)
		if verbose:
			print(myDict)

	if args.humidity:
		logger.info('humidity')
		myDict = getHumidity(logger, verbose, myDict)
		if verbose:
			print(myDict)

	if args.temperature:
		logger.info('temperature')
		myDict = getTemperature(logger, verbose, myDict)
		if verbose:
			print(myDict)

	if args.thermostat:
		logger.info('termostat')
		getThermostat(logger, verbose, myDict)
		if verbose:
			print(myDict)

	if args.all:
		logger.info('all')
		myDict = getLight(logger, verbose, myDict)
		myDict = getHumidity(logger, verbose, myDict)
		myDict = getTemperature(logger, verbose, myDict)
#		myDict = getThermostat(logger, verbose, myDict)
		RRD().rrdUpdate(logger, verbose, myDict, '/opt/projects/monitor/db/monitor.rrd')	
		if verbose:
			print(myDict)
	
if __name__ == '__main__':
	main()
