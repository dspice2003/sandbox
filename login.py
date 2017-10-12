password = ""
limit = 0
while(password != "dinosaur" and password != "rex"):
	username = input("Enter your username\n:")
	password = input("Enter Your Password\n:")
	limit = limit + 1
if(password == "dinosaur" and username=="rex" ):
    print("YOU ARE LOGIN IN")
else:
    print("Access Denied")
