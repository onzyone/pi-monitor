#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime

# ===========================================================================
# Example Code
# ===========================================================================

class DHT:
#	def __init__(self, dhtVesrion, pinNumber):
#		self.dhtVersion	= dhtVersion	# 22
#		self.pinNumber = pintNumber
	def getTempHumidityData(self,value):
		self.value = value
		output = subprocess.check_output(["/opt/projects/lol_dht22/loldht"]);
		matches = re.search(value, output)
		return matches
#Humidity = 34.30 % Temperature = 21.70 *C
	def getTemperature(self):
		tempValue = "Temperature =\s+([0-9.]+)"
		matches = self.getTempHumidityData(tempValue)
	#	matches = self.getMatches(tempValue,output)
	  	temp = float(matches.group(1))
 		return temp

	def getHumidity(self):
		humidityValue = "Humidity =\s+([0-9.]+)"
		matches = self.getTempHumidityData(humidityValue)
#		matches = self.getMatches(humidityValue,output)
		humidity = float(matches.group(1))
		return humidity

