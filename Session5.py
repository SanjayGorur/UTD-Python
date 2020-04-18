#Create a Car class.
class Car:
  def __init__(self, buyerName, color, model, cost):
    self.buyerName = buyerName
    self.model = model
    self.color = color
    self.cost = cost

  def getValues(self):
    print("model -->", self.model)
    print()    
    print("color -->", self.color)
    print()
    print("cost -->", self.cost)
    print()

  def getDiscount(self):
    newPrice = float(int(self.cost)) * 0.70
    return newPrice 

  def changeColor(self):
    print()
    colorChange = input("Choose a color to customize the above car: ")
    self.color = colorChange
    return colorChange


n = int(input("How many cars are you adding: "))
print()
cars = []

for x in range(n):
  name = input("Enter the customer's name: ")
  print()  
  mod = input("Enter the model of your car: ")
  print()
  col = input("Enter the color of your car: ")
  print()
  cos = input("Enter the cost of your car: ")
  print("Car", x + 1, "created!")
  print()
  cars.append(Car(name, mod, col, cos))


for x in range(len(cars)):
  print("Car", x + 1, "\tBuyer's Name:", cars[x].buyerName)
  Car.getValues(cars[x])
  print("Resale price after 30% discount:", Car.getDiscount(cars[x]))
  if(x == int(len(cars)/2)):
    print("Congrats! This car's color is now", Car.changeColor(cars[x]))
  print()

