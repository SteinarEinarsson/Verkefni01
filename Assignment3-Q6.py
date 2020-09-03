a0 = int(input("Input a positive int: "))

print(a0)

while a0 > 1:
    if a0 % 2 == 0:
        a0 = a0 / 2
    else:
        a0 = a0 * 3 + 1
    print(int(a0))
