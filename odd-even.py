number1=int(input("Enter your number1:"))
number2=int(input("Enter your number2:"))


for i in range (number1,number2,+1):
    if i%2==0:
        print(i,"This is even number")
    else:
        print(i, "This is odd number")
