my_list = input("Please Enter 5 Numbers: ").split()

UserNumber = input("Enter the Number to check for: ")

if UserNumber in my_list:
    print("Yes, it exists.")
else:
    print("Sorry, it doesn't exist")