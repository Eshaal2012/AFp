class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
 def __init__(self,fname,lname,year):
    super().__init__(fname,lname)
    self.graduationyear=year
x=Student("Percy","Jackson",2021)
x.printname()
print(x.graduationyear)
y=Student("Harry","Potter",2022)
y.printname()
print(y.graduationyear)