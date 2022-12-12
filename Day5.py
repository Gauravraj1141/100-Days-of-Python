
# Hey we can cut any string at the specific point where we want to trim the string so this method will very helpful for us
str = "my name is gaurav tajput and tt bro is my close friend many more  . and ti sfklsjf"
# we can write place of find and give where we want to trim any string and this method will help for when we work with news api
print(str[0:str.find("many more")])




mystr = "hey my name is gaurav rajput "
ddstr = "hey what is my name"

mystr  = mystr.replace("gaurav","tarun")
print(mystr)
print(mystr.split())
name = "tarun"
print(mystr[mystr.find(name):mystr.find(name)+len(name)])


mycolors = ['red','green','blue',]
print(mycolors)
newcolors = "-".join(mycolors)
print(newcolors)



mystring = "my name is guarav rajput"
strtolist = mystring.split()
print(strtolist)
byjoin = " ".join(strtolist)
print(byjoin)

print(mystring.format())

''' my_list = ["This", "is", "a", "list", "of", "strings"]
You could use the join method to concatenate all the strings in my_list into a single string like this:

Copy code
string = " ".join(my_list)
The join method takes as an argument the string that will be used to join the list of strings together. In the example above, we used the space character (" ") to join the strings together, so the resulting string would be:

Copy code
"This is a list of strings"
You can use any string you want as the separator when concatenating the list of strings together, so if you wanted to use a hyphen instead of a space, you could do it like this:

Copy code
string = "-".join(my_list)
This would produce the following result:

Copy code
"This-is-a-list-of-strings"
Overall, the join method is a useful tool for concatenating a list of strings into a single string in Python.'''



first_name = "gaurav"
s_name = "rajput"
age = 33
info = "Name : {0}{1} , Age :{2} Year old"
formats = info.format(first_name,s_name,age)
print(formats)



# it is very important methods format very interesting :
'''first_name = "John"
last_name = "Doe"
age = 30

info = "Name: {0} {1}, Age: {2}"
formatted_info = info.format(first_name, last_name, age)
In this code, the format method is used to insert the values of the first_name, last_name, and age variables into the info string. The resulting string would be:

Copy code
"Name: John Doe, Age: 30"
The format method is a powerful tool for formatting strings in Python, and it can be used in a variety of different ways to insert values into strings at runtime  
'''