# class # @property @functionname.setter @functionname.deleter

# class user1:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#         print(self.fname)
#         print(self.lname)
#
#     def normal(self):
#         return "anything"
#     @property
#     def fullname(self):
#         return f"{self.fname} {self.lname}"
#
#     @fullname.setter
#     def fullname(self,value):
#         self.fname=value[0]
#         self.lname=value[1]
#
#     @fullname.deleter
#     def fullname(self):
#         del self.fname,self.lname
#
#
#
#
# gr = user1(fname="gaurav",lname="Rajput")
# print(type(gr.fullname))
#
# gr.fullname=("radha","rani")
# print(gr.fullname)
# del gr.fullname
# try:
#     print(gr.fullname)
# except AttributeError:
#     print("'user1' object has no instance fullname")









class Mharana:
    def __int__(self,name):
        self.name = name

        print(self.name)
    @property
    def raj(self):
        return self.name

gr  = Mharana( )
print(gr.name)





