def is_armstrong(number):
	strumber = str(number)
	numberofdigits = len(strumber)
	sum = 0


	for strdigit in strumber:
		digit = int(strdigit)
		sum = sum + (digit**numberofdigits)

	if(sum == int(strumber)):
		#print("Wow, "+strumber+" actually is a armstrong number")
		return 	True
	else:
		#print(strumber + " is pretty armweak")
		return False
def generate_arnstrong_numbers(highend):
	for x in range(highend):
		armstrong = is_armstrong(x)
		if(armstrong == True):
			print(str(x) + " is an armstrong number")

generate_arnstrong_numbers(100000)
generate_arnstrong_numbers(10)
