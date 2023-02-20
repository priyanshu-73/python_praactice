class inout :
	def getstring(self):
		self.b = input('enter string: ')
	def printstring(self):
		print(self.b.upper())

a = inout()
a.getstring()
a.printstring()

