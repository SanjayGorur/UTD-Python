#Stack Program
lis = list(map(int, input("Enter an array of numbers to begin: ").split(" ")))
print("The current list is:   ", lis)
print()

def push(obj):
  lis.append(obj)
  return obj

def pop():
  if(len(lis) == 0):
    return "Sorry, this list is empty"
  return lis.pop(len(lis) - 1)

def peek():
  if(len(lis) == 0):
    return "Sorry, this list is empty"
  return lis[len(lis) - 1]

def repeat():
  check = input("Would you like to ADD, REMOVE, FIND, or STOP? Enter in all caps: ")
  if(check == "ADD"):
    print()
    num = int(input("Please enter the number that you would like to add: "))
    print(push(num), "was added","   \nNew List: ", lis)
    print()
    repeat()

  elif(check == "REMOVE"):
    print()
    if(len(lis) != 0):
      print(pop(), "was removed","   \nNew List: ", lis)
    else:
      print(pop(), "   \nUnchanged List: ", lis)
    print()
    repeat()

  elif(check == "FIND"):
    print()
    print(peek(), "is the top element","   \nUnchanged List: ", lis)
    print()
    repeat()

  elif(check == "STOP"):
    print()
    print("Final List:   ", lis)
    print("You're done! :)")

repeat()


