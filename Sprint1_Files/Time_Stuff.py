def is_leap_year(year):
    # ternary operator
    # if year is evenly divisible by 4, then
    #   if year is also evenly divisible by 100, it is a not leap year unless
    #   it is divisible by 400 as well.
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    # Calculate the days in a particular month (index starts at 1)
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

    # If outside range it's probably a typo.
    elif month in range(1,13):
        if month in (4, 6, 9, 11):
            return 30
        else:
            return 31
    else:
        return 0

def day_of_year(year, month, day):
    days_so_far = 0
    for i in range(1, month):
        days_so_far += days_in_month(i, year)
    days_so_far += day
    return days_so_far

# We can also import a library for this instead.
# https://www.geeksforgeeks.org/find-day-of-the-week-for-a-given-date/?ref=lbp
def day_of_week(y, m, d):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"][(( y + (y // 4) - (y // 100)
             + (y // 400) + t[m - 1] + d) % 7)]
