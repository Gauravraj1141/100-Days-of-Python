# @property @function.setter @function.deleter

class user1:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def normal(self):
        return "anything"
    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @fullname.setter
    def fullname(self,value):
        self.fname=value[0]
        self.lname=value[1]

    @fullname.deleter
    def fullname(self):
        del self.fname,self.lname




gr = user1(fname="gaurav",lname="Rajput")
print(type(gr.fullname))

gr.fullname=("radha","rani")
print(gr.fullname)
del gr.fullname
try:
    print(gr.fullname)
except AttributeError:
    print("'user1' object has no instance fullname")
