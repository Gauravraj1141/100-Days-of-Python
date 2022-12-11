
#Create a calculator

myip = input("Please Choose What do you want to do : \n a. addition\n b. Subtraction\n c. Division\n d. Multiplication\n d. Percentage\nChoose any of these (a,b,c,d,e):")
def mysum(myip):
    operations = ["a","b","c","d"]
    if myip in operations:
        inp1 = int(input("enter first number:"))
        inp12 = int(input("enter second number:"))
        if myip == "a":
            print("Oky You Want to Add these Numbers")
            print("Addition Value : ", inp1 + inp12)
        elif myip == "b":
            print("Oky You Want to Subtract these Numbers")
            if inp1<inp12:
                print("Subtract Value : ",inp12 - inp1)
            else:
                print("Subtract Value : ",inp1 - inp12)

        elif myip == "c":
            print("Oky You Want to Divide these Numbers")
            if inp1<inp12:
                print("divided Value : ",inp12 / inp1)
            else:
                print("divided Value : ",inp1 / inp12)

        elif myip == "d":
            print("Oky You Want to Multipy these Numbers")
            print("multiplied Value : ",inp1 * inp12)

    elif myip == "e":
        inp1 = int(input("Enter Your obtained marks :"))
        inp12 = int(input("Enter Your Maximum marks :"))
        if inp1>inp12:
            print("please enter valid marks")
        else:
            cal = (inp1 / inp12 )*100
            print(f"your marks is {cal} %")

    else:
        print("It is not a valid operation")


mysum(myip)















