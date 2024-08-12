class Complex ():
    def initComplex(self):
        self.realPart = int(input("Enter the Real Part: "))
        self.imgPart = int(input("Enter the Imaginary Part: "))            
    def display(self):
        print(self.realPart,"+",self.imgPart,"i", sep="")
    def sum(self, c1, c2):
        self.realPart = c1.realPart + c2.realPart
        self.imgPart = c1.imgPart + c2.imgPart
    def subtraction(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart
    def multipication(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart
    def division(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart    
c1 = Complex()
c2 = Complex()
c3 = Complex()
c4 = Complex()
c5 = Complex()
c6 = Complex()
print("Enter first complex number")
c1.initComplex()
print("First Complex Number: ")
c1.display()
print("Enter second complex number")
c2.initComplex()
print("Second Complex Number: ")
c2.display()
print("Sum of two complex numbers is ")
c3.sum(c1,c2)
c3.display()
print("Subtraction of two complex numbers is ")
c4.subtraction(c1,c2)
c4.display()
print("Multipication in two number:")
c5.multipication(c1,c2)
c5.display()
print("Division Two Number: ")
c6.division(c1,c2)
c6.display()
