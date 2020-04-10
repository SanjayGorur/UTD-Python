#Find which term of the geometric sequence?

base = int(input("Enter the base value for the geometric sequence: "))

term = int(input("Enter the numeric term within the geometric sequence: "))

multiplier = 0

if(term == 1):
  print("This is the first term of the geometric sequence")

elif(term > 1):
  seqNum = 1
  while((base**multiplier) < term):
    multiplier += 1
    seqNum += 1
  if((base**multiplier) == term):
    print(term, "is term", seqNum, "of the geometric sequence of the base value", base)
  else:
    print(term, "does not exist in this geometric sequence of the base value", base)


