UserInput = int(input("To understand Function capitalize press 1\n To understand Function casefold press 2\n"))



if(UserInput == 1):
	print("Converts the first character to upper case")
	ex = "Hello User"
	print(ex)
	x = ex.capitalize()
	print(x)

elif(UserInput == 2):

	print("Converts string into lower case")
	ex  = "HELLO USER"
	print(ex)
	x = ex.casefold()
	print(x)
