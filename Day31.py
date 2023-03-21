# a = ['ram','shaym']
# b = a.copy()
# # del a
# print(b.__dir__())
# print(id(b))
# # print(a)
#
# print("ram ke gahr{}".format(a))
#
# #
# # print("ram ke  n",end="")
# print("dkdkdkdkddd\r skd")
# print("dkdkdkdkddkd")

#
# # a = ['raja','sheee','sksk',33]
# a = "price is {pricce:2} dol"
# # print(a.strip()) /it removes begining and end spaces
# # print(a.format(price=85))   / price is 85 dol
#
# print(a)

# a = "*&"
# n=20
# for i in range(n):
#     if i < 20:
#         print("  "*(i+1)+a)
#         print("  "*(20-i)+a)
#     if i > 10:
#         print("  "*(i)+a)
#         print("  "*(20-i)+a)
# a = 0
# for i in range(10):
#     if i>0:
#         a +=1
#         print(str(a)*(i))

# rows = 6
#
# for row in range(1,rows):
#     for column in range(row,0,-1):
#         print(column)



# for i in range(4,0,-1):
#     print(i,end='')
# #
# rows = 7
# for row in range(1,rows):
#     for column in range(1,row):
#         print(column,end='')
#     print('\r')





#
#
# import json
#
# pythondict =  {'ram':'raja','rek':333,'dkd':'sdkfjs'}
#
# dubmdata = json.dumps(pythondict)
# print(dubmdata)
# print(type(pythondict))
#
# jsondata ={"ram": "raja", "rek": 333, "dkd": "sdkfjs"}
#
# mypydata = json.loads(str(jsondata))
# print(mypydata)
#


# n = int(input("enter any number:"))

# def Pattern_print(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("* ",end="")
#         print('\r')
#
# Pattern_print(n)

#
# a = 1
# b = 0
#
# try:
#     print(a/b)
# except Exception as e:
#     print(e)








#
# with open('file_name','r')as f:
#     filedata = f.read()
#
# with open('file_name','w')as f:
#     f.write("some else")
#
#     n = 5
#     for i in range(n):
#         print(i)





# #
# a=34
# tp = (3,4,1,a)
# print(tp)



# myfrset = frozenset([3,4,4,4,5,5,9])
# myset = {3,88,33,6}
# myset.add(88888888888)
# myset.update(myfrset)
# print(myset)
# myfrset.add(5555555)
# print(myfrset)
#


# def mydec(calling):
#     def myfun():
#         print("thisisi callable")
#         calling()
#     return myfun
#
#
# @mydec
# def call():
#     print("dkdk")
#
# call()


def func1(myfun):
    return myfun

func2 = func1

del func1
print(func2("dkfjdkjf"))