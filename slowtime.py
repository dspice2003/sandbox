import time



min = input("Enter Number In Minutes\n:")
min = int(min)
for s1 in range(min):
	for s2 in range(6):
		for s3 in range(10):
			print(s1,":",s2,s3)
			time.sleep(0.1)
