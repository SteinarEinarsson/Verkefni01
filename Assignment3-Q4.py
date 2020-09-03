num=int(input("Input an int: "))

x = 1
while x <= num:
    if num % x == 0:
        print(x)
    x += 1