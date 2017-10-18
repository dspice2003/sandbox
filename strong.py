strnumber = input("please enter a number")
sum = 0
for strdigit in strnumber:
	digit = int(strdigit)
	factorial = 1
	for multiplyme in range(1,digit+1):
		factorial = factorial * multiplyme
	print(strdigit+"! ="+str(factorial))
	sum = sum + factorial
if(int(strnumber) == sum):
	print("The number is strong")
else:
	print("The number is not strong")
