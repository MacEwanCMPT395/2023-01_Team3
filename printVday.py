def  main():
    year = input("Enter year: ")
    year = int(year)
    dow = day_of_week(25,5,year)
    date = 25 + (1-dow)
    if (date >=25):
        date = date - 7;
       
    else:
        date = date
        
    print("The date of Victoria Day is: ", date)

def day_of_week(day, month, year):
    '''
     dayOfWeek - Given three integers indicating a date (day, month,
     year), determines which day of the week that day is where 0=Sunday,
     1=Monday, etc
    '''
    a = (14-month)//12
    y = year - a
    m = month + 12*a - 2
    dow = (day + y + y//4 - y//100 + y//400 + 31*m//12) % 7
    dow = dow
    print(dow)
    return dow

main()