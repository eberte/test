# This if my first time using git
# This is very frustrating 
print("Hello")
x = 5
y = 4

# We want to print x and y
print(x, y)


def sum(x, y):
    '''
    Returns the sum of x and y
    '''
    return x+y


def difference(x, y):
    '''
    Returns the difference of x and y
    '''
    return x - y


def product(x, y):
    '''
    Returns the product of x and y
    '''
    return x*y


def factorial(n):
    '''
    Returns the factorial of n. This is a recursive
    function.
    '''
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def abs(x):
    '''
    Returns the absolute value of x.
    '''
    if x >= 0:
        return x
    else:
        return -x

# We are done with the angry comments.
