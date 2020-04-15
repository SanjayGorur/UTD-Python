def make():
  print()
  lis = list(map(int, input("Enter a set of numbers: ").split(" ")))
  print()
  print("Here's your list:", lis)
  print()
  block = input("Type MAGIC to arrange your list in increasing order: ")
  print()
  print()

  count = 0

  def sort(l, count):
    store = 0
    sub = count
    keep = 0
    min = lis[sub]
    while(sub < len(lis)):
      if(min > lis[sub]):
        min = lis[sub]
        keep = sub
      sub += 1
    store = lis[count]
    lis[count] = min
    if(keep != 0):
      lis[keep] = store
    print()
    if(keep != 0):
      print(lis, "Replaced", lis[keep], "with", lis[count])
    else:
      print(lis, "Nothing was changed!")
    return lis[count]

  if(block == "MAGIC"):
    while(count < len(lis)):
      (sort(lis[count:], count))
      count += 1

  print()
  print()
  print("Final List:", lis)
  print()
  print("This selection sort made", len(lis) + 1, "passes to create an ascending list.")
  print()
  print()
  ask = (input("Do you want to try again? --> Yes/No: "))
  if(ask == "Yes"):
    make()
  elif(ask == "No"):
    print()
    print("Hooray! You are done!")

make()
