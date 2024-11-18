a = 9
b = 2
print(a // b)

thislist = ["apple", "bannana", "cherry"]
print(thislist[0:-1])
#unpacking
red, green, blue = thislist
print(red)
print(green)
print(blue)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(type(list3))

thislist2 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist2)

#using * to unpack 
abc = list(("one", "two", "three", "four"))
a, *b, c = abc
print(a)
print(b)
print(c)

a = (9, 0)
b = (9, 8)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

num1 = {1, 2, 3, 4, 5}
num2 = {4, 5, 6, 7}
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)

#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#TUPLE
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#Here TRUE and 1 considered as same value AND same for FALSE
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#DICTIONARY
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict.get("name", "not found"))
print(thisdict.items())
print(thisdict.keys())
print(thisdict.values())
print(thisdict)

for x, y in thisdict.items():
    print(x, y)