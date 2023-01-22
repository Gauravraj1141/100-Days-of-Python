# class User1:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#         print(self.name,self.email)
#
#     @property
#     def ranaji(self):
#         return f"name = {self.name} \n email =  {self.email}"
#
#     @ranaji.setter
#     def ranaji(self , value):
#         self.name = value["name"]
#         self.email = value["email"]
#
#
#
#
# gr = User1(name="GAurav",email="r@gamil.cm")
#
#
# var  = gr.ranaji
# value = {"name":"abhishek","email":"abc@gamil.com"}
# print(var)
#
# print(type(var))
#
#
import time
Hour = int(time.strftime('%I'))
Period = time.strftime('%p')
Minute = int(time.strftime('%M'))
CurrentTime = time.strftime('%I:%M:%S %p')
Name = input("Please enter Your Name: ")
print("The Time is: ", CurrentTime)
if Hour >= 6 and Period == "AM"  and Hour <12 and Minute<= 59:
    print("Good Morning", Name)
elif Hour >= 12 and Period == "PM" and Hour <6 and Minute<= 59:
    print("Good Afternoon ", Name)
elif Hour >= 6 and Period == "PM" and Hour <12 and Minute<= 59:
    print("Good Evening ", Name)
elif Hour >= 12 and Period == "AM" and Hour <6 and Minute<= 59:
    print("Good Night ", Name)