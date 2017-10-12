temp = input("what is the current temperature in celcius?")
temp = float(temp)
isFreezing = temp <= 0.0
isNormal = temp <= 100.0 and  temp > 0.0
isGas = temp > 100.0


if(isFreezing):
	print("ice")
elif(isNormal):
	print("water")
elif(isGas):
	print("air")
else:
	print("I DONT KNOW WHAT THIS IS!!!!")
