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

# This would also be the part where we specify the days we
# do or don't want before creating a dictionary for every
# day of the week.


def create_semester_dates(start_date):
    year = start_date.year
    month = start_date.month
    day = start_date.day

    start_date = datetime.date(year,month,day)

    holidays = Canada(subdiv = "AB",expand = False,years = year, observed=False).items()

    # Add holidays into our list of cancellations
    cancellations = {}

    for date,name in holidays:
    
    # Remove the "unobserved" days of statutory holidays
    
        if date.weekday() < 5:
            cancellations[date] = name
            
        else:
            date = date+datetime.timedelta(days=(7 % date.weekday()))
            cancellations[date] = name

        if name == "Family Day" or name == "Remembrance Day":
            for i in range(1,5):
                cancellations[date+datetime.timedelta(days=i)] = "Reading Week"

    # Create a loop for this. we can maybe create another CSV file for this.
    cancellations[datetime.date(year,9,30)+datetime.timedelta(days=(7 % datetime.date(year,9,30).weekday()))] = "National Day for Truth and Reconciliation"

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

    enddate = start + datetime.timedelta(days=98)

    currdate = start
    while currdate != enddate:
        if not currdate in cancellations.keys():
            dow = currdate.strftime("%A")
            if not dow in ["Friday", "Saturday", "Sunday"]:
                days_of_week[dow][currdate] = []

        currdate = currdate+datetime.timedelta(days=1)

    return days_of_week