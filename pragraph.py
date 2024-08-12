
class person:
    def __init__(self,name,father,mother,Age,Village,District,School,College,University,Hobby):
     self.name=name
     self.father=father
     self.mother=mother
     self.age=Age
     self.village=Village
     self.district=District
     self.school=School
     self.college=College
     self.university=University
     self.hobby=Hobby
    def myfunc(self):
        print(self.name+self.father+self.mother+self.age+self.village+self.district+self.school+self.college+self.university+self.hobby)

a=input("Enter Your Name:")
b=input("Enter Father Name:")
c=input("Enter Mother Name:")
d=int(input("Enter Your Age: "))
e=input("Enter Your Village Name:")
f=input("Enter Your District Name:")
g=input("Enter Your School Name:")
h=input("Enter Your College Name:")
i=input("Enter Your University Name:")
j=input("Enter Your Favorite Hobby:")
p1=person(a,b,c,d,e,f,g,h,i,j)
p1.myfunc()   