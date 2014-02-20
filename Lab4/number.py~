class Integer(object):
	def __init__(self, number ,symbol="+"):
		self.number = number
		self.symbol = symbol
	def display(self):
		print self.symbol + str(self.number)

class NegativeInteger(Integer):
	def __init__(self, number):
		super(NegativeInteger, self).__init__(number, "-")
		self.number = number
	def display(self):
		Integer.display(self)
		print "This is an object of the NegativeInteger class"
		
		
if __name__ =="__main__":
	test = Integer(7, "-")
	test.display()
	x = NegativeInteger(6)
	x.display()
	MyList = [test, x]
	for i in MyList:
		i.display()
	a = int(raw_input("Give me a positive number"))
	c = int(raw_input("Give me a negative number"))
	d = int(raw_input("Give me a minus sign"))
	e = Integer(a)
	f = Integer(c, d)
	e.display()
	f.display()



	
