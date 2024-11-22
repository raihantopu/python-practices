
try:
    x = int(input("tell me your x: "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer.")