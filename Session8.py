# A class like a car -> Model, Cost, MPG, Mileage, Company, [1000, 2000, 1500, 2000]

# Car
# def __init__(Model, Cost, HP, Mileage, Company, [1000, 2000, 1500, 2000])
# Car(,,,,,)
# Car("car1.txt")
# Take these inputs
# storeCar("car1.txt")
# retriveCar("car1.txt")

import pickle

class Car:
  def __init__(self, model=None, cost=None, hp=None, mileage=None, company=None, costList=None):
    self.mod = model
    self.cos = cost
    self.hp = hp
    self.mg = mileage
    self.com = company
    self.coL = costList


  def storeCar(self, fi):
    s = open(fi, "w")
    s.write(self.mod)
    s.write("\n")
    s.write(str(self.cos))
    s.write("\n")
    s.write(str(self.hp))
    s.write("\n")
    s.write(str(self.mg))
    s.write("\n")
    s.write(self.com)
    s.write("\n")
    s.write(str(self.coL))
    s.close()

  def retrieveCar(self, fileName):
    ch = open(fileName, "r")
    look = ch.readlines()
    self.mod = look[0]
    self.cos = float(look[1])
    self.hp = float(look[2])
    self.mg = float(look[3])
    self.com = look[4]
    self.coL = eval(look[5])


  def getParams(self):
    print(self.mod)
    print(self.cos)
    print(self.hp)
    print(self.mg)
    print(self.com)
    print(self.coL)
    print(type(self.coL))
    

# model = input("What is the model of your car\n")
# cost = float(input("What is the cost of your car\n"))
# hp = float(input("What is the horspower of your car: \n"))
# mg = float(input("What is the mileage of your car: \n"))
# comName = input("What your car's company: \n")
# allCost = list(map(int, input("Enter all costs of your car: ").split()))

# cr = Car(model, cost, hp, mg, comName, allCost)
pickle.dump(cr, open("run2.pickle", "wb"))

car2 = open("run2.pickle", "rb")
car = pickle.load(car2)

car.getParams()


# # cr.storeCar("run.txt")

# cr = Car()
# cr.retrieveCar("run.txt")
# cr.getParams()


# def divide(x, y):
#   try:
#     result = x/y
#     print(result)
#   except ZeroDivisionError:
#     print("Division by zero, try again...")
  



# divide(10, 0)

# take user input as list of numbers, save using pickle in a file
# take user input as a file and use pickle and open the file and print the sum of the list

import pickle

# 1 2
# 1 -> input list of numbers, file name to store the numbers
# 2 -> input file name where the list is present and print sum

check = int(input("Enter an integer, 1 or 2: "))

if(check == 1):
  li = list(map(int, input("Enter a set of numbers: ").split()))
  fileName = input("Enter the name of your file: ") + ".pickle"
  temp = open(fileName , "wb")
  pickle.dump(li, temp)
  temp.close()

if(check == 2):
  fileName = input("Enter the name of your file: ") + ".pickle"
  try:
    temp = open(fileName, "rb")
    l = pickle.load(temp)
    print(sum(l))
    div = l[0]
    try:
      for n in range(1, len(l)):
        div = div/l[n]
      print(div)
    except ZeroDivisionError:
      print("Sorry one of your numbers is zero.")

  except FileNotFoundError:
    print("Sorry, your file has not been found.")
