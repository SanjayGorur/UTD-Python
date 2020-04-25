class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def getGraduation(self):
    print(self.graduationyear)

x = Student("Kuldeep", "Yadav", 2020)
x.printname()
x.getGraduation()


# Circle -> radius
# Circle1 -> getArea()
# Circle2 -> getCircum()

class Circle:
  def __init__(self, radius):
    self.rad = radius
  def printR(self):
    print(self.rad)

class Circle1(Circle):
  def __init__(self, radius):
    super().__init__(radius)

  def getArea(self):
    print("Area of circle:", 3.14 * self.rad ** 2)

class Circle2(Circle):
  def __init__(self, radius):
    super().__init__(radius)

  def getCircum(self):
    print("Circumference of circle: ", (6.28 * self.rad))

circ = Circle1(6)
circ.getArea()

circ = Circle2(6)
circ.getCircum()


class Base1:
  def __init__(self):
    self.str1 = "Base1"
    print(self.str1)

class Base2:
  def __init__(self):
    self.str2 = "Base2"
    print(self.str2)

class Derived(Base1, Base2):
  def __init__(self):
    print("Derived")
    Base1.__init__(self)
    Base2.__init__(self)

Derived()


#Car -> 
#Boat ->
#Hybrid -> 

class Car:
  def __init__(self):
    self.hp1 = 200
    print(self.hp1)

class Boat:
  def __init__(self):
    self.hp2 = 500
    print(self.hp2)

class Hybrid(Car, Boat):
  def __init__(self):
    Car.__init__(self)
    Boat.__init__(self)

  def getCarP(self):
    print("Car's engine price:", self.hp1 * 100)

  def getBoatP(self):
    print("Boat's engine price:", self.hp2 * 250)

  def getTotal(self):
    print("Hybrid price:", (self.hp1 * 100) + (self.hp2 * 250))

mix = Hybrid()

mix.getCarP()
mix.getBoatP()
mix.getTotal()


f = open('sample.txt', 'r')
message = f.read()
print(message)
f.close()

print("")

f = open('sample.txt', 'r')
message = f.readlines()
print(message)
f.close()

file = open("sample2.txt", 'w')
file.write('Line 1\n')
file.write("Line 2\n")
file.close()

with open('sample2.txt', 'r') as f:
  message = f.read()
  print(message)


file = open("sanjay.txt", 'w')
file.write("Hi, my name is Yaru\n")
file.write("I attend Otto\n")
file.write("I am going to Stanford!\n")
file.close()

file = open("cap.txt", "r")
message = file.readlines()
file.close()
fi = open("copy.txt", "w")
for i in message:
  fi.write(i)
fi.close()

f = open("sample.txt", "a")
for i in range(10):
  f.write(str(i))
  f.write("\n")
f.close()

#write method takes strings only.


fil = open("sample.txt", "r")
mess = fil.readlines()

num = int(mess[-1])

fil.close()
fil = open("sample.txt", "a")

check = num + 10
for n in range(num, check):
  fil.write(str(n))
  fil.write("\n")

fil.close()
