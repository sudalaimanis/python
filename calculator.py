# Basic calculator program using Python functions

def addition(a1, b1):
    return a1+b1

def subtraction(a1,b1):
    return a1-b1

def multiplication(a1,b1):
    return a1*b1

def devision(a1,b1):
    return a1/b1

print("math operations\n")

print("1. addition\n"
      "2. subtraction\n"
      "3. multiplication\n"
      "4. devision\n"
      )

operation = int(input("enter your operation 1,2,3,4: "))

c1 = float(input("enter your first number: "))
c2 = float(input("enter your second number: "))

if operation == 1:
    print(c1, "+", c2 ,"=", addition(c1, c2))
elif operation == 1:
    print(c1, "+", c2 ,"=", addition(c1, c2))
elif operation == 1:
    print(c1, "+", c2 ,"=", addition(c1, c2))
elif operation == 1:
    print(c1, "+", c2 ,"=", addition(c1, c2))
else:
    print("Invalid number")
