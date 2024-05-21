class Person:
  def __init__(self, fname, lname,age):
    self.firstname = fname
    self.lastname = lname
    self.age = age
 
  def printname(self):
    print(self.firstname, self.lastname)
 
class Student(Person):
  def __init__(self, fname, lname, age, year, gpa):
    super().__init__(fname, lname,age)
    self.graduationyear = year
    self.gpa = gpa
 
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear, ". Your GPA is", self.gpa, "and you are", self.age)
 
x = Student("Mike", "Olsen",25, 2019, 3.8)
x.welcome()