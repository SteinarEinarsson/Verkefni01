#for i in range(0,1):
#    print(i)

#the_max = int(input("Enter the upper limit: "))
#the_sum = 0
#extra = 0

#for number in range(1, the_max):
#    if number%2 == 1:
#        the_sum = the_sum + number
#    else:
#        extra = extra + 1
#
#print(the_sum, extra)


#for i in range(4):
#    print("a")
#    for j in range(2):
#        print("b")


#the_sum = 0
#for i in range(0,5):
#    if i==2:
#        continue
#    else:
#        the_sum += i
#print(the_sum)

#for i in range(6, 0, -2):
#    print(i, end=" ")

#length = len(range(1,6))
#print(length)



#highest = int(input("Input an int: "))

#for i in range(1, highest):
#    if (i%3):
#        print(i)



max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

 #Fill in the missing code
days_when_amount_acquired = 0
the_sum = 0
factor = 1

for i in range(max_days):
    the_sum += factor
    factor = factor * 2
    
    if the_sum >= target:
        days_when_amount_acquired = i+1
        break

print('Days needed:',days_when_amount_acquired)


#num = int(input("Input an int: ")) # Do not change this line

#the_sum = 0

#for i in range(num+1):
#    the_sum=0
#    for ii in range(i+1):
#        the_sum += ii
#    if the_sum != 0:
#        print(the_sum)


#length = int(input("Input the length of series: "))

#the_sum = 0
#the_number = 2

#for i in range(length):
#    print(the_number)
 #   the_sum += the_number
#    if the_number < 0:
#        the_number = (the_number *-1)+2
#    else:
#        the_number = (the_number *-1)-2
#print("sum: " +str(the_sum))