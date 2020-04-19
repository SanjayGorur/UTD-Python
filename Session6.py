
class Stack:
  def __init__(self, size):
    self.size = size
    self.arr = []

  def push(self, obj):
    if(len(self.arr) == 0):
      self.arr.append([obj, obj])
    elif(self.size < len(self.arr) - 1):
      return False
    else:
      self.arr.append([obj, min(self.arr[-1][1], obj)])
    return self.arr

  def pop(self):
    if(len(self.arr) == 0):
      return False
    return self.arr.pop(-1)

  def peek(self):
    if(len(self.arr) == 0):
      return None
    return self.arr[-1]

  def findMin(self):
    if(self.arr):
      return self.arr[-1][1]
    return None
    

siz = int(input("Enter your preferred size of the stack: "))
if(siz == -1):
    print("You are done!")

else:
  stac = Stack(siz)
  while True:
    numCom = int(input("Enter a number: "))
    if(numCom == 1):
      print(stac.push(input("Enter the object you would like to add: ")))
    elif(numCom == 2):
      print(stac.pop())
    elif(numCom == 3):
      print(stac.peek())
    elif(numCom == 4):
      print(stac.findMin())
    elif(numCom == -1):
      break
    else:
      print("Sorry, you entered an invalid number")
    
