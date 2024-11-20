# class Student:
#     name = ""
#     gpa = 0.0

# x = Student()
# x.name = "Topu Raihan"
# x.gpa = 5.0
# print("Name: ", x.name, "GPA: ", x.gpa)

class Student:
    def setValue(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def displayValues(self):
        print("name: ", self.name, "gpa: ", self.gpa)

x = Student();
x.setValue("Topu Raihan", 5.0)
x.displayValues()

class Test:
    def __init__(self) -> None:
        self.name = "topu raihan"
    
    def display(self):
        print("name is: ", self.name)

x = Test()
x.display()

class Test2(Test):
    def display2(self):
        print(self.name + " from test2 class")

x = Test2()
x.display()
x.display2()