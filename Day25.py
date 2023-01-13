"""'''doc string'''

def myfun():
    '''hey it is a doc string and we should write it before the function body and after the function start'''
    print("hey doc string ")

myfun()
print(myfun.__doc__) #so it will print docstring we can write it in class function and module also


"""
# 0,1,1,2,3,5
# recursion
def fibo(n):
    if (n==0 ):
        return  0
    elif (n==1):
        return 1

    else:
        return  fibo(n-1) + fibo(n-2)

print(fibo(3))











