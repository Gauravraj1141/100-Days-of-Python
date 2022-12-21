'''# Default Arguments in function
# it is default argument function even we give argument then it cosider our argument if we don't give any argument then it will take default argument which we give in this function
def myfun(a=8,b=5):
    print("average is ",(a+b)/2)

# here we call simple function without arguments
myfun()
# here we call function with arguments
myfun(4,55)

# if we want to give only one value and second value will be default value
myfun(a=5)
# if we want to give only one value and second value will be default value
myfun(b=25)


# keyword arguments
# we can give any argument without any order
# so here we give initially b and after that a
myfun(b = 44,a=2323)



# required argument

def newfun(a,b=3,c=34):
    print(a+b+c)
    print("here a is :",a , "here b is :",b,"here c is:",c)

# so here a is required argument and b and c is not mandatory argument because we give default value in it
newfun(c=232,a =33,b=44)

'''


# args and kwars

'''
def numbers(*nums):
    print(nums)
    sum = 0
    for i in nums:
        sum = sum + i
    print("sum",sum)
    print(len(nums))
    print(sum/len(nums))



# so if we give a tuple of list in this args argument then it will convert it into a tuple
asd = (3,23,34,43,42,42,42,425,25,252524254)

numbers(3,23,34,43,42,42,42,425,25,252524254)
# here we need to give args with this star*
numbers(*asd)

'''


'''
# kwargs
# in kwargs we can give key and values in it and it returns dictonary

def mykeywordarguments(**students):
    print(students)
    for i , j in students.items():
        print(f"{i} ka ghar {j} me h")


dict = {"ram":"kalyanpur","gaurav":"ghosipur","shiva":"bhaguvala"}
mykeywordarguments(**dict)
mykeywordarguments(ramu="najibabad",ghodi = "astabal")
'''

