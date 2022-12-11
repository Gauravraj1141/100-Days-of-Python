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
str.title(): Converts the first character of each word in a string to uppercase and all other characters to lowercase.
str.strip(): Removes leading and trailing whitespace from a string.
str.replace(old, new): Replaces all occurrences of a specified string with another string.
str.split(delimiter): Splits a string into a list of substrings based on a specified delimiter.
str.join(iterable): Joins the elements of an iterable (such as a list or tuple) into a string, using a specified separator.
str.format(): Formats a string using placeholders and values provided as arguments.
str.startswith(substring): Returns True if a string starts with a specified substring, or False otherwise.
str.endswith(substring): Returns True if a string ends with a specified substring, or False otherwise.
str.find(substring): Returns the index of the first occurrence of a specified substring in a string, or -1 if the substring is not found.
str.index(substring): Returns the index of the first occurrence of a specified substring in a string, or raises a ValueError if the substring is not found.
str.isalpha(): Returns True if a string contains only alphabetic characters, or False otherwise.
str.isdigit(): Returns True if a string contains only digits, or False otherwise.
str.islower(): Returns True if all the characters in a string are lowercase, or False otherwise.
str.isupper(): Returns True if all the characters in a string are uppercase, or False otherwise.
str.isspace(): Returns True if a string contains only whitespace characters, or False otherwise.
str.istitle(): Returns True if a string is in title case (i.e., the first letter of each word is capitalized), or False otherwise.
These are just some of the many string methods available in Python. To learn more about string methods and how to use them, you can refer to the Python documentation or try out some examples on your own..'''


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