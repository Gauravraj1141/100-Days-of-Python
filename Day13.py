import math

def calculator(operation,digit1,digit2):
    if operation == "+":
        return digit1+digit2
    elif operation == "-":
        if digit1>digit2:
            return digit1-digit2
        elif digit2>digit1:
            return  digit2-digit1
        elif digit2 == digit1:
            return 0
    elif operation == "*":
        return digit1*digit2
    elif operation == "/":
        if digit1>=digit2:
            return (digit1/digit2)
        elif digit2>=digit1:
            return  digit2/digit1



while True:
    op = input("please select any one of these \n+\n-\n*\n/ :")
    digit1 = int(input("enter your number"))
    digit2 = int(input("enter your second number"))
    print(calculator(op,digit1,digit2))
    userchoice = input("if you want to quit this calculator press 'y' otherwise press anythingelse:")
    if userchoice=="y":
        print("Thanks for using my calculator")
        break
    else:
        continue
