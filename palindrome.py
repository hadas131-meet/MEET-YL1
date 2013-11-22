def palindrome():
	a=raw_input("enter a word")
	b=a
	a=a[::-1]
	if b==a:
		print "True"
	else:
		print "False"
if __name__=="__main__":
	palindrome()	

	

