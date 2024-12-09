class Student:
    ...

def main():
    student = getStudent()
    print(f"{student.name} from {student.house}")

def getStudent(): 
    student = Student()
    student.name = getName()
    student.house = getHouse()
    return student

def getName():
    return input("enter name: ")

def getHouse():
    return input("enter house: ")


if __name__ == "__main__":
    main()