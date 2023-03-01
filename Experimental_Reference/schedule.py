from Time_Stuff import days
import Classes
from open_csv import programs, classrooms
import closest_sum

print()
print(programs,"\n")
print(classrooms,"\n")

for i,j in days.items():
    print(i,j,"\n")

class Schedule:
    def __init__(self, student, degree, program, courses, classrooms):
        self.student = student
        self.degree = degree
        self.program = program
        self.courses = courses
        self.classrooms = classrooms

