# Strings are immutable
'''Here are some common string methods in Python:

str.lower(): Converts the string to lowercase.
str.upper(): Converts the string to uppercase.
str.strip(): Removes leading and trailing whitespace from the string.
str.isalpha(): Returns True if the string contains only alphabetic characters, and False otherwise.
str.isdigit(): Returns True if the string contains only numeric digits, and False otherwise.
str.isnumeric(): Returns True if the string contains only numeric characters, and False otherwise.
str.isspace(): Returns True if the string contains only whitespace characters, and False otherwise.
str.startswith(prefix): Returns True if the string starts with the specified prefix, and False otherwise.
str.endswith(suffix): Returns True if the string ends with the specified suffix, and False otherwise.
str.find(substring): Returns the index of the first occurrence of the specified substring within the string, or -1 if the substring is not found.
str.replace(old, new): Replaces all occurrences of the specified old string with the specified new string.
str.split(delimiter): Splits the string into a list of substrings based on the specified delimiter.
These are just some of the many string methods available in Python. For a complete list, you can refer to the official Python documentation.'''


str = 'my nameis3423 gaurv rajput'

print(str[2:5:])

a = "!!!!!harry!!!!!!!"
print(a)
a = a.upper()
# it remove all left exclamatin marks
b = a.lstrip("!")
# it remove all right exclamatin marks
c = a.rstrip("!")

print(b)
print(c)
# it convert a string in to the list
print(str.split())

#first letter capitalize
print(str.capitalize())

print(len(str))

print(str.center(33))
print(len(str.center(33))) #33
print(len(str)) #22

if str.endswith("name" , 0,7):
    print("yes rajput is in the last of this string ")


if str.startswith("my"):
    print("yes my is in the start of this string ")


print(str.find('gaurav'))
print(str.isprintable())
print(str.isascii())
print(str.isalnum())

mystr = '       dfg'

print(mystr.isspace())





sk = 'Tkill Fam Rm'
# if all the starting words of string will capital then it will true otherwise false;
print(sk.istitle()) # true

dk  = 'dkkd skd skdjf'
print(dk.istitle())  # false




mynew = "my name is gaurava rajput"
 # it will convert this in title case
print(mynew.title())  #My Name Is Gaurava Rajput