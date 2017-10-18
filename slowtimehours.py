import time


hours = input("enter number of hours\n:")
hours = int(hours)

for h1 in range(hours):
	for m1 in range(6):
		for m2 in range(10):
			for s2 in range(6):
				for s3 in range(10):
					print(h1,":",m1,m2,":",s2,s2)
					time.sleep(.001)
