# In Python, the ord() function returns the Unicode code point for a given Unicode character. For example, ord('a') would return the code point for the character 'a', which is 97. This function can be useful for working with characters and their corresponding code points in Unicode.

d = ord('z')-ord("a")+1
print(d)
print(ord("a"))
print(ord("z"))


print(hex(2))
print(oct(2))
mystr = "123456789"

print(tuple(mystr))
ope = tuple(mystr)
for i in ope:
    print(int(i)*2)
    print(int(i)+2)


dd = 'erkeskjdflsv'
print(set(dd))