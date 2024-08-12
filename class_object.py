
class person:
    def __init__(self,name,id):
     self.name=name
     self.id=id
    def myfunc(self):
        print("Your Name Is",self.name)
        print("Your Id Is",self.id)
a=input("Enter Your Name:")
b=int(input("Enter Your Id: "))
p1=person(a,b)
p1.myfunc()   