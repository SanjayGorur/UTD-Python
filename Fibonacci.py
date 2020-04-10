#Find the nth term of the fibonacci sequence

check = int(input("Enter a number: "))

if(check == 1 or check == 2):
  print("Term", check,  "of the sequence is 1.")

elif(check >= 3):
  track = 3
  firstTerm = 1
  secondTerm = 1
  sum = 0
  while(track <= check):
    sum = firstTerm + secondTerm
    if(track % 2 == 0):
      secondTerm = sum
    else:
      firstTerm = sum
    track += 1
  print("Term", check,  "of the sequence is", sum)

else:
  print("Sorry, you entered an invalid term.")
