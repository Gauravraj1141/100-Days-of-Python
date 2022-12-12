# now one man get up 5pm so we disscuss on his daily routine
# In Python, conditional operators are used to evaluate a boolean expression and return a result based on the outcome of the evaluation. The most common conditional operators are if, else, and elif (short for "else if").
# here some conditional operator :
# ( <= ,  >= ,  <  , > , == ,  != )


a = 9
print(a>8) # True
# so these are conditional operator it gives result in boolean like true or false:



getup = int(input("Tell Us Time : "))

if getup >= 5 and getup<=8:
    if getup >=5 and getup <=6:
        print("Please go for running")
    elif getup <= 8 and getup >=6:
        print("Please go for some walk")

elif getup <=5:
    print("please go for meditation and then start runnning")
elif getup >=9 and getup <=11:
    if getup >= 10 and getup <=11:
        print("you are late please do your daily work")
    else:
        print("hey you are very late")
else:
    print("please adjust your time")
