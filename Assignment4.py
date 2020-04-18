#Find whether there exist 3 numbers in a list that collectively sum to a 'target' value.

repeat = True

def go():
  print()
  lis = list(map(int, input("Enter a set of numbers: ").strip().split(" ")))

  print()
  print(lis)

  print()
  target = int(input("Select a sum target for 3 numbers of the list: "))

  def findNums(li, tar):
    s = set()
    for x in range(len(li) - 2):
      for y in range(x + 1, len(li) - 1):
        num = tar - li[x] - li[y]
        if(num in s and num != li[x] and num != li[y]):
          print()
          print(li[x], "+", li[y], "+", num, "=", tar, "\t You did it!")
          print()
          return True
        else:
          s.add(li[y + 1])
    print()
    print("Sorry. 3 numbers in the list don't add up to the target")
    print()
    return False

  findNums(lis, target)

go()

while(repeat):
  check = input("Would you like to try again? Please respond yes or no: ")

  if(check == "yes"):
    go()
  else:
    print()
    print("Hooray! You are done!")
    print()
    repeat = False
