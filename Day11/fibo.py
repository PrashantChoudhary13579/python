#  Here we are learning about the modules in Python

def fib(n):
    a, b = 0, 1
    while a < n :
        print( a , end = " " )
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0,1
    while a<= n:
        result.append(a)
        a,b = b, a+b
    return result

fib(7)
fib2(7)
