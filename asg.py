# # # def evens():
# # #     for i in range(1,10):
# # #         if i%2==0:
# # #             print(i)
# # #
# # #
# # # evens()
# #
# str =  'amarjeet, MCA,  New Delhi, India'
#
# lst = str.split("  ")
# print(lst)
# #
# # param = ['name','qualification','State','Country']
# # # dicts = {'name': lst[0], 'qualification': 'MCA', 'State': 'New Delhi', 'Country': 'India'}
# # print(dict['State'])
# # mydict = dict(zip(param,lst))
# # print(mydict)
#
#
# # class School:
# #     def __init__(self , name, cls):
# #         self.name = name
# #         self.cls = cls
# #
# #     def peon(self):
# #         return "raj"
# #
# # gr = School("ram","rr")
# # print(gr.peon())






payload = {}

mytc = 'kdkdkd'
mydict  = {'tickets':mytc}

myconv = []
for i in range(44):
    conv = "raji"
    for j in range(33):
        attach = 'attach'
    myconv.append(conv)

payload['mytickets'] = mydict
payload['mytickets']['myconv'] = myconv

print(payload)

