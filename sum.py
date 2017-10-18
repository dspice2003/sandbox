adding = True
sum = 0
while(adding):
	num1 = input("please enter a number")
	num1 = int(num1)
	sum = sum + num1
	print(sum)
	print("Add again? yes or no")
	add_again = input()
	adding = add_again == "yes"
