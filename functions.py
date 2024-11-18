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