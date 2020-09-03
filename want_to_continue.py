want_to_continue_str = 'y'

# Repeat till the user enters n
while want_to_continue_str == 'y':
    # Read input again
    want_to_continue_str = input('\nWould you like to continue (y/n)? ')
    # Check if continue is NO
    if want_to_continue_str=='n':
        break
    # Read all the data
    costumer_code = input("Customer code: ")
    number_of_days = input("Number of days: ")
    odometer_start = input("Odometer reading at the start: ")
    odometer_end = input("Odometer reading at the end: ")
    # Calculate miles driven
    miles_driven = int(odometer_end) - int(odometer_start)

    # Check if the code is for budget
    if costumer_code == 'b':
        budget_charge = 40
        base_charge = int(number_of_days) * int(budget_charge)
        milage_charge = float(miles_driven) * 0.25
        
    # Check if the code is for daily
    elif costumer_code == 'd':
        daily_charge = 60
        base_charge = int(number_of_days) * int(daily_charge)
        average_miles = (float(miles_driven)) / (float(number_of_days))
        if float(miles_driven) <= 100:
            extra_miles = 0
        else:
            extra_miles = float(miles_driven) - 100
        milage_charge = (float(extra_miles) * 0.25) * float(number_of_days)
    else: # Invalid if d or b is not entered
        print("Invalid Customer code. Please try again.")
        continue
    amount_due = float(base_charge) + float(milage_charge)

    # Print the information
    print("Welcome to car rentals!")
    print("Customer code: ", costumer_code)
    print("Number of days: ", number_of_days)
    print("Odometer reading at the start: ", odometer_start)
    print("Odometer reading at the end: ", odometer_end)
    print("Amount due: ", amount_due)