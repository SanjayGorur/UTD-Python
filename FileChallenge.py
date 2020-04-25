#2 text files used --> "input.txt" and "output.txt"

def repeat():
  print()
  check = input("Do you want to continue? yes or no: ")
  if(check == "yes"):
    run()
  else:
    print()
    print("Hooray! You are done!  :)")

def run():
  fl = open("input.txt", "w")
  fl.write("Hello, what is your name?")
  fl.close()

  print()
  with open("input.txt", "r") as f:
    print(f.read())
  f.close()
  print()

  fi = open("output.txt", "w")

  name = input("Enter your name: ").strip()
  fi.write("My name is ")
  fi.write(name)

  fi.close()

  print()
  with open("output.txt", "r") as fil:
    print(fil.read())
  fil.close()
  print()

  file = open("input.txt", "a")

  file.write("\n")
  file.write("Nice! Now, How old are you?")

  file.close()

  with open("input.txt", "r") as filef:
    message = filef.readlines()
    print(message[-1])
  print()
  filef.close()

  filefi = open("output.txt", "a")
  filefi.write("\n")
  age = int(input("What is your age: "))
  filefi.write("I am ")
  filefi.write(str(age))
  filefi.write(" years old!")
  filefi.close()

  with open("output.txt","r") as filefil:
    newMess = filefil.readlines()
    print()
    for x in newMess:
      print(x)
  repeat()

run()
