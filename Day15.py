'''myl = [3,2,4,4,2,"ram","shyam","radha",32,323,444,56,66]

print(myl[-12:5])
print(myl[0:len(myl)-5])
print(len(myl))'''

# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])
'''
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)'''


'''tt = (33,2,3,4,34,23,23,23,23)
result = [i for i in tt if i%2==0]
print(result)


om = [342,23,4,423,23,2,34,32,23,2323]
reu = [i for i in om if i!=23]
print(reu)'''

'''names = ["Milo", "Sarah", "Bruno", "Anastasia", "Ros"]
namesWith_O = [item for item in names if (len(item) > 4)]
a = namesWith_O.append("ramu")
print(namesWith_O)'''

'''
mylist = ["radha","guarav","tomar","tanisha","pooja","bhopendra"]
short_names = [name.capitalize() for name in mylist if len(name)<8 and name.startswith("t") ]
short_names.append("radha")
print(short_names)

short_names.sort()
print(short_names)

'''
num_list = [2,3,5,2,4,3,43,422,23,425,5,2,23,4,25,24,24,22]
newlist = [23,34,24,23,23,23]

print(len(num_list))
# pop return the remove value and it by default remove last value but we give 0 index value remove
# k = num_list.pop(0)
# print(k)
print(num_list)
# it clear all the list value and our list lenth is now 0
# remove = num_list.clear()

# we can insert value in our list we insert newlist in our num_list at index 5
# and insert this value on index 2
'''insertlist = num_list.insert(5,newlist)
insertlist2 = num_list.insert(2,2541)'''


# it add the newlist at the end of this num_list and it returns none
num_list.extend(newlist)

# so here k  is the reference of our numlist if we change in this k then num_list will change because this k only takes reference of our list

k = num_list

k[0] = "ram"
print(num_list)


# if we use this .copy method then the value of this will come inside that var and then not effect of base list
m = num_list.copy()
m[1]  = 'shaym'
print(m)
# so here don't effect on our base list
print(num_list)

print(len(num_list))
print(num_list)



