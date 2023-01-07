YourName = str(input("Please Enter Your Good Name: "))
YourAge = int(input("Please enter your age:"))
if (YourAge >= 18 and YourAge < 21):
    print("Congratulation !", YourName, "Your Can Drive")
elif(YourAge >= 21 and YourAge <= 30):
    print("Congratulation !", YourName, "You Can drive and also you can do marrige.\nHappy Married Life in Advance")
elif (YourAge > 30 and YourAge < 120):
    print("Congratulations !", YourName, "You can drive")
elif (YourAge >= 120):
    print("No !", YourName, "You can not drive because you are dead")
elif (YourAge < 18):
    print("No !", YourName, "You can not drive, Please Wait for ", 18 - YourAge, "Years more to drive")
else:
    print(YourName, "Please Enter Valid Age or a Valid Name")