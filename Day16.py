mytup = (1,2,31,2,3)
mytup2 = (1,2,31,2,3)
mytup3 = (1,2,31,2,3)

# we use zip for combine some variable and take together same place objects

a = zip(mytup,mytup2)
print(dict(a))


print(mytup[2:])

# so we use sorted here for sort this tuple  because sort attribute  is not present in this tuple
print(sorted(mytup,reverse=True))
print(sorted(mytup,reverse=False)) #it is by default false
# print(mytup.sort()) #AttributeError: 'tuple' object has no attribute 'sort'