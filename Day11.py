# i = 5
# j = 22


# it will execute till condition will be false means if condition will true then it will execute
# so we use here 1 or True means both are true then it will run infinite
# while(1):
#     print('hey it is i',i,"and it is j",j)
#     j -= 1
#     i += 1


import  time

a = time.time()

# for i in range(8760):
#     print("ram")

# while loop wins because it is some faster than for loop
# in it time takes while loop this : 7.6014368534088135
# i = 0
# while(i<100000):
#     print("jai shree ram",i)
#     print(time.time()-a)
#     i +=1



# in it time takes for loop this : 7.867778778076172
# for j in range(100000):
#      print("jai shree ram sita",j)
#      print(time.time()-a)






# new_value = 66
#
# while(new_value>5):
#     new_value -=2
#     print(new_value, "and how it decrease you can see the value of new_value")
#
# else:
#     print("when while loop condition will false then this else will execute print thsi line ")

# hey dowhile loop in python doesn't exist but we can make a do while loop in python let's see how emulate it:
# in dowhile loop condition will true always first time means when we run dowhile loop then the codition will true or not but dowhile's loop content will run and then it checks the conditon
#
# i = 3
# print(i)
# # so content of loop one time will run wheather condition ture or not
# while(i<3):
#     print(i)

# other languages do while loop


# do{
#     # loop body
#     # so this loop body will always run if condition true or not
# }while(condition);



# here we emulate do while loop


'''
str  = 'gaurav'
count = 0

while True:
    print("this line first time wheather condition true or not ")
    i = input("enter str : ").lower()
    count += 1

    if str == i:
        break
    elif str != i and count > 7:
        break'''


# here we use continue means if name will gaurav means correct then loop will run other wise it will break means continue will break iteration ye loop continue se laut jata h or firse loop chal jata h
i = 0
while True:
    print("this line will be print ")
    name = input("enter your name: ").lower()
    i +=1
    if name == "gaurav":
        print("hey i found your name")
        continue

    break



