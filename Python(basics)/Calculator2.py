# making a better calculator

num1 = float(input("Enter the number:"))
num2 = float(input("Enter the number:"))
op = input("Enter the operator:")

if(op == "+"):
    print(num1+num2)
elif(op == "-"):
    print(num1-num2)
elif(op == "*"):
    print(num1*num2)
elif(op == "/"):
    print(num1/num2)
else:
    print("Invalid input")