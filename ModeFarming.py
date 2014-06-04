
"""
	Code for self-help group management of coffee farmers.
	By Rodgers Andati.
"""

class Farmer:
	""" A class to hold a farmer's details """
	def __init__(self, name, farmerID, nextFarmer=None):
		self.name = name
		self.farmerID = farmerID
		self.nextFarmer = nextFarmer

	def __str__(self):
		return "Name: "+ self.name+", No: "+ str(self.farmerID)

class FarmersCollection:
	""" Collection class for all farmers in the village """
	numOfFarmers = 0
	def __init__(self, numOfBags=2, daysInterval=1):
		self.numOfBags = numOfBags
		self.daysInterval = daysInterval
		self.firstFarmer = None
		self.lastFarmer = None
		self.nextReceiver = None

	def addFarmer(self,name):
		"""Addition of a new farmer"""
		FarmersCollection.numOfFarmers += 1
		farmer = Farmer(name, FarmersCollection.numOfFarmers)
		if self.firstFarmer != None:
			self.lastFarmer.nextFarmer = farmer
			self.lastFarmer = farmer
		else:
			#First farmer being added
			self.firstFarmer = farmer
			self.lastFarmer = farmer
			self.nextReceiver = farmer

	def removeFarmer(self,name):
		"""Removal of an existing farmer"""
		farmer = self.firstFarmer
		#Check if first farmer
		if farmer.name == name:
			self.firstFarmer = self.firstFarmer.nextFarmer
			#check if was next receiver
			if farmer == self.nextReceiver:
				self.nextReceiver = farmer.nextFarmer
			del farmer

			#Change numbering of farmers to reflect new order
			tempFarmer = self.firstFarmer
			while tempFarmer != None :
				tempFarmer.farmerID -= 1
				tempFarmer = tempFarmer.nextFarmer
		else:
			previous = farmer
			while farmer != None :
				if(farmer.name == name):
					previous.nextFarmer = farmer.nextFarmer

					#check if was next receiver
					if farmer == self.nextReceiver:
						self.nextReceiver = farmer.nextFarmer

					del farmer #garbage collection
					FarmersCollection.numOfFarmers -= 1 #Decrement count of farmers

					#Change numbering of farmers to reflect new order					
					tempFarmer = previous.nextFarmer
					while tempFarmer != None :
						tempFarmer.farmerID -= 1
						tempFarmer = tempFarmer.nextFarmer
					break
				previous = farmer
				farmer = farmer.nextFarmer
				if farmer == None:
					print "*** No such farmer\n"
	def getNextReceiver(self):
		"""Returns who is next to receive coffee of bags """
		print "Next Receiver:- ", self.nextReceiver, "\n"

	def received(self, name):
		if self.nextReceiver.name == name:
			if self.nextReceiver.nextFarmer != None: #Check if the last farmer
				self.nextReceiver = self.nextReceiver.nextFarmer
			else:
				self.nextReceiver = self.firstFarmer
		else:
			print "*** You are violating the order! "+ self.nextReceiver.name + " is to receive next.\n"	

	def printFarmers(self):
		""" Iteration over all the farmers and printing their number"""
		print "List of farmers"
		print "--------------------------"
		farmer = self.firstFarmer
		while farmer != None :
			print farmer
			farmer = farmer.nextFarmer

	def getPreviousFarmer(self):
		""" Returns the previous receiver """
		farmer = self.firstFarmer
		if farmer == self.nextReceiver:
			print "Previous receiver :- ", self.lastFarmer, "\n"
		else:
			previous = farmer
			while farmer != None :
				if farmer == self.nextReceiver:
					print "Previous receiver :- ", previous, "\n"
				previous = farmer
				farmer = farmer.nextFarmer

	def nextReceiverInDays(self,days):
		"""Returns whose turn it will be in X days from now"""
		numdays = days % FarmersCollection.numOfFarmers
		if numdays == 0: #the current next receiver is the one
			print "Receiver in " + str(days) + " days is:- ", self.nextReceiver.nextFarmer, "\n"
		else:
			farmer = self.firstFarmer
			for x in range(0, numdays):
				if farmer.nextFarmer != None:
					farmer = farmer.nextFarmer
				else:
					farmer = self.firstFarmer

			print "Receiver in " + str(days) + " days is:- ", farmer, "\n"

#IMPLEMENTATION SECTION
farmers = FarmersCollection() #Instance of the collection
print "" #new line

#Add farmers, remove some
farmers.addFarmer("Joseph")
farmers.addFarmer("Rodgers")
farmers.addFarmer("Faith")
farmers.addFarmer("Vincent")
farmers.addFarmer("Mildred")
farmers.addFarmer("Janet")
farmers.addFarmer("Andrew")

farmers.removeFarmer("Joseph")
farmers.removeFarmer("Mildred")


farmers.received("Rodgers")

#Print farmers
farmers.printFarmers()
print "" #new line

farmers.getNextReceiver()
farmers.getPreviousFarmer()
farmers.nextReceiverInDays(8)

