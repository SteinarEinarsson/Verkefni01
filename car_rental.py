print('Welcome to car rentals!')
contine_str = 'y'

while contine_str == 'y':
    contine_str = input('Would you like to continue (y/n)? ')
    if contine_str == 'n':
        break

    customer_code = input('Customer code (b or d): ')
    number_days = input('Number of days: ')
    Odo_start = input('Odometer reading at the start: ')
    Odo_end = input('Odometer reading at the end: ')
    miles_total = int(Odo_end) - int(Odo_start)

    if customer_code == 'b':
        budget_cost = 40
        base_cost = int(budget_cost) * int(number_days)
        miles_cost = float(miles_total)*0.25
        amount_due = round((float(base_cost) + float(miles_cost)),1)
        print('Miles driven:', miles_total,'\nAmount due:',amount_due)



    elif customer_code == 'd':
        daily_cost = 60
        base_cost = int(daily_cost) * int(number_days)
        av_miles = float(miles_total) / float(number_days)
        if float(av_miles) <= 100:
            extra_miles = 0
            amount_due = float(base_cost) + float(miles_cost)
            print('Miles driven:', miles_total,'\nAmount due:',amount_due)

        else:
            extra_miles = (float(miles_total) / float(number_days)) - 100
            miles_cost = float(extra_miles) * float(number_days) * 0.25
            amount_due = float(base_cost) + float(miles_cost)
            print('Miles driven:', miles_total,'\nAmount due:',amount_due)








