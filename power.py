def add (x,y):
	z = x+y
	return z 

def multiply(a,b):
	total = 0
	for x in range(a):
		total = add(total,b)
	return total

def power(base,exponenent):
	total = 1
	for x in range(exponenent):
		total = multiply(total,base)
		print(total)
	return total


print(power(3,4))
#print(multiply(20,20))
