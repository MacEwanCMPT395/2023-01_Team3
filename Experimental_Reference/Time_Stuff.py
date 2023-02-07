'''
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
    
'''

'''
Holidays:

New Year's Day (Observed)
Family Day
Good Friday
Easter Monday
Victoria Day
Canada Day (Observed)
Heritage Day
Labour Day
National Day for Truth and Reconciliation (SEPT 30)
Thanksgiving Day
Remembrance Day Observed
Christmas Day
Dec 26-31 (christmas)

Reading Week Winter (4 days after Family Day)
Reading Week Fall (4 days after Remembrance Day)
'''
# While I was proud of my time conversions, with the use of
# the datetime library, we don't need to do these conversions
# anymore :)

import datetime
from holidays import Canada

holidays = Canada(subdiv = "AB",expand = False,years = 2023).items()

# Add holidays into our list of cancellations
cancellations = dict(holidays)

for date,name in holidays:
    
    # Remove the unobserved days of holidays.
    if " (Observed)" == name[-11:]:
        cancellations.pop(date)
                
    if name == "Family Day" or name == "Remembrance Day":
        for i in range(1,5):
            cancellations[date+datetime.timedelta(days=i)] = "Reading Week"
            
            
year = 2023
cancellations[datetime.date(year,9,30)] = "National Day for Truth and Reconciliation"

days = {
    "Monday":[],
    "Tuesday":[],
    "Wednesday":[],
    "Thursday":[],
    "Friday":[],
    "Saturday":[],
    "Sunday":[],
}

# Semester start and end determined by the user.
# semester start: Jan 3
# semester end: April 4 (classes, not including exams)
start = datetime.date(2023,1,3)
enddate = datetime.date(2023,4,4)

currdate = start
while currdate != enddate:
    if not (currdate in cancellations):
        days[currdate.strftime("%A")].append(
            {currdate:"Classroom List"})

    currdate = currdate+datetime.timedelta(days=1)

    
#print(days)
#print(len(days["Monday"]))
