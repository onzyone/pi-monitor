import rrdtool, os

class RRD():
#	def __init__(self, myDict):

	def rrdCreate(self, fname):
		ret = rrdtool.create(fname, "--step", "60", "--start", '0',
			"DS:temps1:GAUGE:120:-40:50",
			"DS:temps2:GAUGE:120:-40:50",
			"DS:hums1:GAUGE:120:0:100",
			"DS:lux1:GAUGE:120:0:40000",
			"RRA:AVERAGE:0.5:1:2880",
			"RRA:AVERAGE:0.5:6:700",
			"RRA:AVERAGE:0.5:24:775",
			"RRA:AVERAGE:0.5:144:1500",
			"RRA:AVERAGE:0.5:288:2000",
			"RRA:MIN:0.5:1:600",
			"RRA:MIN:0.5:6:700",
			"RRA:MIN:0.5:24:775",
			"RRA:MIN:0.5:144:1500",
			"RRA:MIN:0.5:288:2000",
			"RRA:MAX:0.5:6:700",
			"RRA:MAX:0.5:24:775",
			"RRA:MAX:0.5:144:1500",
			"RRA:MAX:0.5:288:2000")
		return ret 
	
	def rrdExport(self, fname):
		print 'File: %s' %(fname)
	

	def rrdUpdate(self, logger, verbose, myDict, fname):
		if verbose:
			print 'File: %s, Values: %s' %(fname, myDict)
		if not os.path.isfile(fname):
			print 'No File: %s, making it now' %(fname)
			ret = self.rrdCreate(fname)
			if ret:
				logger.error('failed to make rrd file: str(rrdtool.error())')
#'light': 256.819, 'thermostat': 23.611, 'temperature': 21.8, 'humidity': 60.3
		temperature = myDict.get('temperature')
#		thermostat = myDict.get('thermostat')
		thermostat = 0 
		humidity = myDict.get('humidity')
		light = myDict.get('light')
		ret = rrdtool.update(fname, 'N:%s:%s:%s:%s' %(temperature, thermostat, humidity, light));
		if ret:
			logger.error('failed to update rrd: str(rrdtool.error())')
	

