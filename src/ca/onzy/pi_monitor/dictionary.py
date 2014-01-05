class Dictionary:
	def newDict(self):
		newDict = dict()
		return newDict

	def updateDict(self, myDict, key, value):
		temp = {key : value}
		myDict.update(temp)
		return myDict
