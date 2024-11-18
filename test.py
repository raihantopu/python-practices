import math
import calendar as c

# x = 2.5;
# print(math.ceil(x))
# print('test run')

# print(c.calendar(2024))

n = 13
for i in range(1, 4):
    for j in range(1, n + 1):
        if(i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print("*", end = "")
        else:
            print(" ", end = "")
    print()
#if else practice for grade check for checking grade
#m = 90;
m = int(input("please enter a number to check you grade: "))
if(m >= 90):
    print("you have got A++")
elif(m >= 80 and m < 90):
    print("you have got A+")
elif(m >= 70 and m < 80):
    print("you have got A")
elif(m >= 60 and m < 70):
    print("you have got A-")
elif(m >= 50 and m < 60):
    print("you have got B")
elif(m >= 40 and m < 50):
    print("you have got C")
elif(m >= 33 and m < 40):
    print("you just passed by your ear and got D")
else:
    print("you have failed!!!!! sorry!!!")

#case practice 
lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

#multiple and condition match
a = 10
b = 11
c = 12
if(a > 0 and b > 0 and c > 0):
    print("AND condition matched")
else:
    print("there is a problem matching conditions")

#OR condition 
if(a > 0 or b > c):
    print("OR condition matched")
else:
    print("OR condition is not matched")

#when 
if not (a % 3 == 0 or a % 5 == 0):
    print("if condition mathed but we are expecting that TURE will be fliped to FALSE cause we are using not")
else:
    print("when condition matched then this will print")

#while loop 
count = 0
while count < 10:
    print("count is now: ", count)
    count += 1


n = 100
sum = 0
i = 1
while i <= n:
    sum = sum +i
    i = i + 1

print(sum, i)