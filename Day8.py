str1 = 'Gaurav Rajput'
str2  = 'gaurav rajput'
print(str1 == str2) #it gives False becasue both are diff case

print(str1.casefold() == str2.casefold()) #it gives True becasue we use casefold it convert in to the lower case both string


# now we disscuss on the match case  in python 3.10 new method like  case and switch method

var1 = int(input("Enter your age"))

match var1:
    case 44:
        print("hey you are adult")

    case 34:
        print("hey you are young")

    case _ if var1 >20 and var1<50:
        print("hey you are our youth and change our generation")

    case _ if var1 > 60 and var1 < 90:
        print("hey you are some old please rest")

    case _:
        print("you will go ")



