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
holidays = Canada(subdiv = "AB",expand = False,years = 2023).items()

# Add holidays into our list of cancellations
cancellations = dict(holidays)

'''
for date,name in holidays:
    print(date,name)
'''

for date,name in holidays:
    
    # Remove the "observed" days of holidays.
    if " (Observed)" == name[-11:]:
        cancellations.pop(date)

    if name == "Family Day" or name == "Remembrance Day":
        for i in range(1,5):
            cancellations[date+datetime.timedelta(days=i)] = "Reading Week"
       
year = 2023
# Create a loop for this. we can maybe create another CSV file for this.
cancellations[datetime.date(year,9,30)] = "National Day for Truth and Reconciliation"

'''
print()
for date,name in cancellations.items():
    print(date,name)
'''
# This would also be the part where we specify the days we
# do or don't want before creating a dictionary for every
# day of the week.
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
            {currdate:[]})
        

    currdate = currdate+datetime.timedelta(days=1)

'''
print(days)

sum = 0
for i in days.keys():
    sum+= len(days[i])

print(sum)

print(len(days["Monday"]))

'''
