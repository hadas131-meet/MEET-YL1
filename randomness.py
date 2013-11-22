from random import randint
def randomness():
		a=randint(1,2)
		if a==1:
			print "H"
		else:
			print "T"
if __name__=="__main__":
	while True:
		n=raw_input("Type n")
	    if n=="n":
		     randomness()
