import main

def my_function():
    print("this is from my_function")

print("this is not in the function")

my_function()


def my_function2(name):
    print("hello: ", name)


my_function2("topu")

#return function
def addTwoValues(n1, n2):
    return n1 + n2

x = addTwoValues(5, 5)
print(x)

def addAndMult(n1, n2):
    '''
    this comment is considered as docstring 
    this will used as reference material for other users who will use it, like what this function does, what will be the return type
    what user can expect from this function etc.
    '''
    sum = n1 + n2
    mult = n1 * n2
    return sum, mult
print(addAndMult.__doc__)
x, y = addAndMult(2, 3)
print(x, y)

print(main.add(1, 2))

print(main.cube(5))

lambda_cube = lambda x: x * x * x
print(lambda_cube(2))

multipParameterLambda = lambda a, b, c: a + b + c
print(multipParameterLambda(4, 5, 6))

def getLength(a):
    return len(a)
x = map(getLength, ("acb", "afdlkdjlf", "jldlkh"))
print(list(x))

def square(a):
    return a * a

x = list(map(square, (1, 3, 4, 5)))
print(x)

def getAges(x):
    if x < 18:
        return False
    else:
        return True
    
ages = [5, 6, 7, 10, 20, 40]
adults = list(filter(getAges, ages))
print(adults)