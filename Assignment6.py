class CircQ:

  def __init__(self, size):
    self.size = size
    self.Qu = []
  
  def front(self):
    if(self.isEmpty()):
      return -1
    return self.Qu[0]

  def rear(self):
    if(self.isEmpty()):
      return -1
    return self.Qu[-1]

  def enQueue(self, obj):
    if(self.isFull()):
      return False
    self.Qu.insert(0, obj)
    return True
  
  def deQueue(self):
    if(self.isEmpty()):
      return False
    print()
    print(self.Qu.pop(0), "was removed")
    return True
  
  def isEmpty(self):
    return len(self.Qu) == 0

  def isFull(self):
    return len(self.Qu) == self.size

k = int(input("Please set the size of your queue: "))

if(k == -1):
  print("You are done!")

else:
  Q = CircQ(k)
  while True:
    print()
    check = input("Enter a command--front, rear, add, remove, end: ")
    if(check == "front"):
      print("Current List: ", Q.Qu)
      if(Q.front() == -1):
        print()
        print("Sorry, but there are no elements to peek.")
      else:
        print()
        print("Front element: ", Q.front())
    elif(check == "rear"):
      print("Current List: ", Q.Qu)
      if(Q.rear() == -1):
        print()
        print("Sorry, but there are no elements to peek.")
      else:
        print()
        print("Last element: ", Q.rear())
    elif(check == "add"):
      print("Current List: ", Q.Qu)
      value = int(input("Enter a number to add to the queue: "))
      if(Q.enQueue(value) == False):
        print()
        print("Sorry, but you can't add any more elements.")
      else:
        print()
        print("Updated Queue:\t", Q.Qu)
    elif(check == "remove"):
      print("Current List: ", Q.Qu)
      if(Q.deQueue() == False):
        print()
        print("Sorry, but there are no elements to remove.")
      else:
        print()
        print("Updated Queue:\t", Q.Qu)
    elif(check == "end"):
      print()
      print("You are done!")
      break
    else:
      print("Sorry, the command you entered is invalid.")

