import datetime
from holidays import Canada

'''
Notes:

We can import a CSV of holidays/cancellations, import the holidays, double check them, and add any more.
We can use this method to also let the user define a set of days that could be cancelled for whatever reason they want.
That's why we had the extra National Day for Truth and Reconcilation day added after. It will be a set
of user made cancellations.
In a CSV this would look like:
Name, month, day
The year will be automatically determined in the actual program.
'''
year = 2023
holidays = Canada(subdiv = "AB",expand = False,years = year).items()

# Add holidays into our list of cancellations
cancellations = {}

for date,name in holidays:
    
    # Remove the "unobserved" days of statutory holidays
    if date.weekday() < 5:
        cancellations[date] = name

    if name == "Family Day" or name == "Remembrance Day":
        for i in range(1,5):
            cancellations[date+datetime.timedelta(days=i)] = "Reading Week"

# Create a loop for this. we can maybe create another CSV file for this.
cancellations[datetime.date(year,9,30)] = "National Day for Truth and Reconciliation"


# This would also be the part where we specify the days we
# do or don't want before creating a dictionary for every
# day of the week.

def create_semester_dates(start_date):
    days_of_week = {
        "Monday":{},
        "Tuesday":{},
        "Wednesday":{},
        "Thursday":{}
    }

    # Semester start and end determined by the user.
    # semester start: Jan 3
    # semester end: April 4 (classes, not including exams)

    start = start_date

    while start in cancellations:
        start = start+datetime.timedelta(days=1)

    enddate = start + datetime.timedelta(weeks=13)

    currdate = start
    while currdate != enddate:
        if not (currdate in cancellations):
            dow = currdate.strftime("%A")
            if not dow in ["Friday", "Saturday", "Sunday"]:
                days_of_week[dow][currdate] = []

        currdate = currdate+datetime.timedelta(days=1)

    return days_of_week

#days = create_semester_dates(datetime.date(2023,1,3))
'''
print(days)

sum = 0
for i in days.keys():
    sum+= len(days[i])

print(sum)

print(len(days["Monday"]))

'''
