# # Abstract base class
#
# from abc import  ABC , abstractmethod
#
#
# class empsalary(ABC):
#      def __init__(self,name,email):
#          self.name = name
#          self.email = email
#
#
#      @abstractmethod
#      def salary(self):
#         pass
#
# class emp(empsalary):
#      def __init__(self,name,email,address,profession):
#          super().__init__(name,email)
#          self.address = address
#          self.profession = profession
#
#      @property
#      def salary(self):
#          return f"emp name is {self.name} and he is {self.profession}"
#
#      def __str__(self):
#          return self.name
#
#
#
# gr = emp(name = "gaurav",email="rajput@gmail.ocm",address="ramnagar",profession="Python Django developer")
#
# print(gr.salary)



#
#
# class Animal(ABC):
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Cat(Animal):
#     def __init__(self, name, breed, toy):
#         super().__init__(name, species="Cat")
#         self.breed = breed
#         self.toy = toy
#
#     def make_sound(self):
#         print(f"{self.name} makes a meow sound.")
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, species="Dog")
#         self.breed = breed
#
#     def make_sound(self):
#         print(f"{self.name} makes a bark sound.")




# class emp:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     @property
#     def position(self):
#         if self.salary <2000:
#             return "vaiter"
#         else:
#             return "Software engineer"
#     @position.setter
#     def position(self,newvalue):
#         self.salary = newvalue
#
#
# gr = emp("gaurav",5000)
# print(gr.position) #Software engineer
# # so here we give new value in this position so it returns now vaiter
# gr.position = 1000
# print(gr.position) #vaiter



# class mail:
#     def __init__(self,name):
#         self.name = name
#     @property
#     def email(self):
#         return f"{self.name}@gmail.com"
#     @email.setter
#     def email(self,ip):
#         nm = ip.split("@")[0]
#         self.name = nm
# person = mail("gauravrajput2771")
# print(person.email)
# person.email = input("enter your name =  ")
# print(person.email)
#


# class Employee:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{self.fname}{self.lname}@gmail.com"
#     def log(self):
#         return f"this is employee {self.fname},{self.lname}"
#     @property
#     def email(self):
#         return f"{self.fname}{self.lname}@gmail.com"
#     @email.setter
#     def email(self,string):
#         print("setting now.....")
#         name = string.split("@")[0]
#         self.fname = name.split(".")[0]
#         self.lname = name.split(".")[1]
#
# gr = Employee("gaurav ","rajput")
# gr.fname = "bhatti"
# print(gr.email)
# gr.email = "punit.doon@gmail.com"
# print(gr.email)

#
#
# from abc import  ABC , abstractmethod
# class user1(ABC):
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     @abstractmethod
#     def fullname(self):
#         return f"{self.fname} {self.lname}"
#
#
# # here we give values in tuple in this setter
#
# class myusr(user1):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
#     @property
#     def fullname(self):
#         return super().fullname()
#     @fullname.setter
#     def fullname(self,values):
#         self.fname=values[0]
#         self.lname=values[1]
#
# data = myusr(fname="gaurav",lname="rajput")
# print(data.fullname)
# data.fullname = ("rajput","guarv")
# print(data.fullname)
#
#
# # here we give values in dictionary in this setter
# class myusr2(user1):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)
#     @property
#     def fullname(self):
#         return super().fullname()
#     @fullname.setter
#     def fullname(self,dict):
#         self.fname=dict["value1"]
#         self.lname=dict["value2"]
#
# data = myusr2(fname="gaurav",lname="rajput")
# print(data.fullname)
# data.fullname = {"value1":"vinay","value2":"rajput"}
# print(data.fullname)



class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def log(self):
        return f"this is employee {self.fname},{self.lname}"
    @property
    def email(self):
        if self.fname == None  or self.lname == None:
            return "it is no any emailid please use setter to manage this again "
        else:
            return f"{self.fname}{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("setting now.....")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]
    @email.deleter
    def email(self):
        del  self.fname , self.lname


gr = Employee(fname="gaurav",lname="rajput")
print(gr.email)
del gr.email
try:
    print(gr.email)

except AttributeError:
    print("'Employee' object has no instance email'")
