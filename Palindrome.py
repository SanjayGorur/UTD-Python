
pal = input("Enter the string for which you wish to check if palindrome: ")

def checkP(palin):
  for num in range(0, int((len(palin)/2)) + 1):
    if(palin[num] != palin[len(palin) - num - 1]):
      print()
      print("Sorry your inputed string is not a palindrome.  :(")
      return False
  print()
  print("Hooray! The string that you entered is a palindrome!")
  return True

checkP(pal)

while True:
  print()
  ask = input("Do you want to continue? yes or no: ")
  if(ask == "yes"):
    print()
    pal = input("Enter the string for which you wish to check if palindrome: ")
    checkP(pal)
  else:
    print()
    print("You are done!")
    break
