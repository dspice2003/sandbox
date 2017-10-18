number = input("please enter a number:")
length = len(number)
x = 0

totalsum= 0
while(x < length):
	numbertoadd = int(number[x])
	totalsum = totalsum + numbertoadd
	x=x+1
print(totalsum)
