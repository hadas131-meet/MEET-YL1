def divisors(n):
    for i in range (1,n):
        if n%i==0:
           print i
if __name__=="__main__":
	divisors(int(raw_input("enter a number")))
