num = int(input("Enter an odd number: "))

check = 1

for n in range(1, num + 1):
    addUp = int(num - n)
    print(addUp * "|", check * "*", addUp * "|")
    check += 2
