class CourseCapacity:
# The idea is to check the capacity of the rooms offered for a PROGRAM SPECIFIC course on the first day
# With the most hours needed.
# Ex. PRDV 0201 for Project Management (PM) add up all those room capacities
# Students enrolled in that course shold not be taking that course twice
# So other rooms teaching that specific course in the same day is another cohort in the program
# and we "SHOULD" have the max capacity for PM program
# No need to check all the other classes...hopefully.
    def __init__(self, course_name):
        self.course_name = course_name
        self.course_capacity = 0

    def add_course(self, room_capacity):
        self.course_capacity += room_capacity
        print(self.course_capacity)

        return self.course_capacity

    def max_cap(self):
        print(self.course_capacity)
        program_status = "Course: {} capacity: {}.".format(self.course_name, self.course_capacity)
        return program_status


prdv0201 = CourseCapacity('PRDV 0201')
prdv0201.add_course(5)
prdv0201.add_course(5)

print(prdv0201.max_cap())
