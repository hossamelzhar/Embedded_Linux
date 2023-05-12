#Get Num1 and Num 2
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num1: "))

#print Bitwise Operations
print("Bitwise AND"+ str(num1&num2))
print("Bitwise OR"+ str(num1|num2))
print("Bitwise XOR"+ str(num1^num2))
print("Bitwise NOT"+ str(~num1))
print("Bitwise NOT"+ str(~num2))

#print Arth. Operations
print("SUM"+ str(num1+num2))
print("SUB"+ str(num1-num2))
print("MUL"+ str(num1*num2))
if(num2 != 0):
	print("DIV"+ str(num1/num2))
	
#print Logical Operations
print((num1>num2))
print((num1<num2))
print((num1>=num2))
print((num1<=num2))
