# def guru(arg):
#     print(arg,"it is a grs")
#
# raju = guru
#
# raju("hey")
#
#
# def func1():
#     print("kss")
#     print("hey i am func",func1())
#
#
# func1()
import copy

#
# def division(x,y):
#     print(x+y)
#
# def innerdiv(func):
#     def inner(x,y):
#         if x<y :
#             return func
#         return inner
# div = innerdiv(division)
# div(5,8)
#


# def divide(x,y):
#     print(x/y)
# def outer_div(func):
#     def inner(x,y):
#         if(x<y):
#
#             x,y = y,x
#
#             return func(x,y)
#
#     return inner
# divide1 = outer_div(divide)
# # divide1(2,4)
#
#
# def func1(fun):
#     print("it decorator fun")
#     fun()
#     print("aftert hsi func")
#
# @func1
# def myfun():
#     print("this is simple ")
#
#

#
# dc = dict(zip(['tokens', 'Notification'], [{'new_access_token': ''}, "Hellow World"]))
# print(dc)
# ip = {"access_token":"rakdsdfjlaskjf"}
# dc['tokens']['new_access_token'] = "sldfjs"
# print(dc)
#
# # some most commen thing in python dict with zip function
# mydict = dict(zip(['name','email'],[{"firstname":"","lastname":""},"gaurav@gamil.com"]))
# mydict["name"]["firstname"] = "Gaurav"
# mydict["name"]["lastname"] = "Rajput"
# print((mydict["name"]["firstname"]))
#
#
# print(2%7)


# days = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
# print(days[5])


# def solution(S, K):
#     days = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
#     digit = K%7
#     for day in days:
#         if day == S:
#             newdigit = days.index(day)+digit
#             if newdigit > 7 :
#                 return days[days.index(day)+digit-8]
#             else:
#                 return days[days.index(day)+digit]
#
# print(solution("Sat",99))




a = {"raj":"raji","rank":44}
print(type(a))
data = copy.deepcopy(a)
print(data.__dir__())
print(type(data))








