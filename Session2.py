# Take 3 numbers as input and print the largest number

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

# if(x >= y and x >= z):
#   print("The greatest number is: ", x)

# elif(y >= x and y >= z):
#   print("The greatest number is: ", y)

# else:
#   print("The greatest number is: ", z)

if(x >= y):
  if(x >= z):
    print("The greatest number is: ", x)
  else:
    print("The greatest number is: ", z)

elif(y >= x):
  if(y >= z):
    print("The greatest number is: ", y)
  else:
    print("The greatest number is: ", z)  

    for n in  range(51, 101, 2):
  print(n)


  
num = 51

while(num < 100):
  print(num)
  num += 2


x = int(input("Enter a number: "))


for n in range(x + 1):
  for m in range(n + 1):
    print("*", end = "")
  print("")


  for n in range(1, x + 1):
  print(n * "*")


  x = int(input("Enter a number: "))

for num in range(1, 11):
  print(num, " * ", x, " =", num * x)


# ^^Weekly Assignment^^
#    *
#   ***
#  *****
# *******

# nested for loop
# multiple for loops inside the first for loop
