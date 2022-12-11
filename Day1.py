# In Python all the things means datatypes are object
# complex numbers
a = 22 + 34j
b = 224 + 934j
cp = complex(a)
print(cp.imag)
print(cp.real)
print(cp.conjugate())
print(a+b)

print(type(b))
c = 33
d = "ddd"
e = True
f = None
g = 3.33
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
k = {"data":{"raja":"raj"}}
print(k["data"])
print(type(k["data"]))

to = ("gaurav",23,234,44,33.4234,3223,2323,23j)
li = ["gaurav",23,234,44,33.4234,3223,2323,23j]
print(to[4])
li[2] = 33

print(
li[2])



