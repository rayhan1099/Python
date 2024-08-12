
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastName = lastname

    def setName(self,name):
        self.name=name

    def setLastName(self,lastname):
        self.lastName=lastname

    def getName(self):
        print('Name',self.name)

    def getLastName(self):
        print('LastName',self.lastName)


class Student(Person): 
    def __init__(self,name,lastname,university):
        self.university = university
        Person.__init__(self, name, lastname)

    def setuniversity(self, university):
        self.university=university

    def getuniversity(self):
        print("My name is",self.name, self.university)
        

def main():
    student = Student("Rayhan","Islam", "Reptto")
    student.setuniversity("BAUSTIAN")
    student.getuniversity()
main()
