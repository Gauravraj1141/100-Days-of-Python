class user1:
    def __init__(self , name,score=0):
        self.playername = name
        self.score = score

    @property
    def userdata(self):
        try:
            return f" name is {self.playername} \n Player score is: {self.score}"

        except AttributeError:
            print("hey you have no values ")


    @userdata.setter
    def userdata(self,values):
            self.playername = values["name"]
            self.score += values["score"]

    @userdata.deleter
    def userdata(self):
        del self.playername,self.score



name = input("enter player name:")
gr = user1(name =name)
while True:
    out = input("user out or not [y/n]:")
    if out == "y":
        print(f"hey {gr.playername} score is : {gr.score} ")
        break

    Score = int(input("enter your score"))
    values = {"name":name,"score":Score}
    gr.userdata = values
    print(gr.userdata)










