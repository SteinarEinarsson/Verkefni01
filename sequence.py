n = int(input("Enter the length of the sequence: ")) # Do not change this line

num = 1
num2 = 2
num3 = 3
num4 = 0
print(num)
print(num2)
print(num3)
for i in range(1,n-2):
    num4 = num+num2+num3
    num = num2
    num2 = num3
    num3 = num4
    print(num4)