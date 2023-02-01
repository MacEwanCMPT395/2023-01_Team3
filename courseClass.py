class Student:
    def __init__(self, student_id, name, degree, program):
        self.student_id = student_id
        self.name = name
        self.degree = degree
        self.program = program

class Degree:
    def __init__(self, degree_id, core_courses):
        self.degree_id = degree_id
        self.core_courses = core_courses

class Program:
    def __init__(self, program_id, max_capacity, courses):
        self.program_id = program_id
        self.max_capacity = max_capacity
        self.courses = courses

class Course:
    def __init__(self, course_id, max_capacity, term_id, transcript_hours, lecture_duration):
        self.course_id = course_id
        self.max_capacity = max_capacity
        self.term_id = term_id
        self.transcript_hours = transcript_hours
        self.lecture_duration = lecture_duration

class Classroom:
    def __init__(self, classroom_id, capacity, lab_room):
        self.classroom_id = classroom_id
        self.capacity = capacity
        self.lab_room = lab_room

'''
Notes from Graham:

Considering the time_slot thing, we should make the time slots 
and days being taught specific to the course/class itself.
i.e. class can only be taught between a certain hour at certain days of week.
We can do this using a white list of days not including holidays or cancellations
which we will account for. The question is how to organize this data.
I'll make my own pull requests with my edits later today.
'''
class Schedule:
    def __init__(self, student, degree, program, courses, classrooms):
        self.student = student
        self.degree = degree
        self.program = program
        self.courses = courses
        self.classrooms = classrooms
        self.schedule = {}
        self.time_slot = {"Monday": {"start": 8, "end": 17},\
             "Tuesday": {"start": 8, "end": 17}, \
            "Wednesday": {"start": 8, "end": 17}, \
            "Thursday": {"start": 8, "end": 17},}

    # def generate_schedule(self):
    #     schedule = []
    #     for course in self.courses:
    #         for classroom in self.classrooms:
    #             if classroom.capacity >= course.max_capacity:
    #                 schedule.append((course, classroom))
    #                 break
    #     return schedule

    def schedule_courses(self):
        # loop through all classrooms in the instance
        for classroom in self.classrooms:
            # loop through days "Monday" and "Wednesday"
            for day in ["Monday", "Wednesday"]:
                # select courses that belong to PCOM degree
                pcom_core_courses = [course for course in self.degree.core_courses if self.degree.degree_id == "PCOM"]
                # loop through PCOM courses
                for course in pcom_core_courses:
                    # check if the course can be scheduled on the current day and classroom
                    schedule_on_day = self.check_availability(course, day, classroom)
                    if schedule_on_day:
                        # check if the time slot for the course is available on the current day and classroom
                        if self.check_time_slot(course, day, classroom):
                            # schedule the course on the current day and classroom
                            self.schedule_course(course, day, classroom)
                        else:
                            print(f"Cannot schedule {course.course_id} on {day}")

            for day in ["Tuesday", "Thursday"]:
                bcom_core_courses = [course for course in self.degree.core_courses \
                    if self.degree.degree_id == "BCOM"]
                for course in bcom_core_courses:
                    schedule_on_day = self.check_availability(course, day, classroom)
                    if schedule_on_day:
                        if self.check_time_slot(course, day, classroom):
                            self.schedule_course(course, day, classroom)
                        else:
                            print(f"Cannot schedule {course.course_id} on {day}")



    def check_availability(self, course, day, classroom):
    # Check if the given day exists in the schedule
        if day in self.schedule:
            # Iterate over all courses scheduled for the day
            for scheduled_course, scheduled_classroom in self.schedule[day]:
                # Check if the scheduled course is in the same classroom as the given classroom
                if scheduled_classroom == classroom:
                    # Calculate the end time of the scheduled course
                    end_time = scheduled_course.lecture_start_time + scheduled_course.lecture_duration
                    # Check if the lecture start time is within the time slot and the end time is within the time slot
                    if scheduled_course.lecture_start_time <= end_time <= self.time_slot[day]["end"]:
                        return False
        # If the day does not exist in the schedule or there is no overlap, return True
        return True


def check_time_slot(self, course, day, classroom): 
    # Check if the day is already in the schedule
    if day in self.schedule:
        # Iterate through each scheduled course for the given day
        for scheduled_course, scheduled_classroom in self.schedule[day]:
            # Check if the same classroom is scheduled
            if scheduled_classroom == classroom:
                # Calculate the end time of the scheduled course
                end_time = scheduled_course.lecture_start_time + scheduled_course.lecture_duration
                # Check if the scheduled course overlaps with the new course
                if scheduled_course.lecture_start_time < end_time and end_time <= self.time_slot[day]["end"]:
                    # If there is an overlap, return False
                    return False
    # If there is no overlap, return True
    return True


def schedule_course(self, course, day, classroom):
    # Get the start time of the time slot for the given day
    start_time = self.time_slot[day]["start"]
    
    # Calculate the end time of the course
    end_time = start_time + course.lecture_duration
    
    # Check if the end time of the course exceeds the end time of the time slot for the given day
    if end_time > self.time_slot[day]["end"]:
        print(f"Cannot schedule {course.course_id} on {day} as the end time exceeds the time slot end")
        return False

    # Check if the given day already has any courses scheduled
    if day in self.schedule:
        # If it does, loop through each scheduled course and classroom
        for scheduled_course, scheduled_classroom in self.schedule[day]:
            # Check if the scheduled classroom is the same as the one provided
            if scheduled_classroom == classroom:
                # If it is, calculate the end time of the scheduled course
                scheduled_course_end_time = self.time_slot[day]["start"] + scheduled_course.lecture_duration
                # Check if the start time or end time of the new course overlaps with the scheduled course
                if start_time < scheduled_course_end_time and end_time > scheduled_course_end_time:
                    print(f"Cannot schedule {course.course_id} on {day} as it overlaps with {scheduled_course.course_id}")
                    return False
        # If the new course does not overlap with any other courses, add it to the schedule for the given day
        self.schedule[day].append((course, classroom))
    else:
        # If no courses are scheduled for the given day, create a new entry in the schedule dictionary with the new course and classroom
        self.schedule[day] = [(course, classroom)]
    # Update the start time of the time slot for the given day to be the end time of the new course
    self.time_slot[day]["start"] = end_time
    return True




# # Test 1: Testing student class
# student = Student(1, "John Doe", "BCOM", "PM")
# assert student.student_id == 1
# assert student.name == "John Doe"
# assert student.degree == "BCOM"
# assert student.program == "PM"

# # Test 2: Testing degree class
# degree = Degree("BCOM", ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
# assert degree.degree_id == "BCOM"
# assert degree.core_courses == ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"]

# # Test 3: Testing program class
# program = Program("PM", 100, ["PRDV 0201", "PRDV 0202", "PRDV 0203"])
# assert program.program_id == "program1"
# assert program.max_capacity == 100
# assert program.courses == ["PRDV 0201", "PRDV 0202", "PRDV 0203"]

# # Test 4: Testing course class
# course = Course("PCOM 0203", 50, "Term 1", 15, 1.5)
# assert course.course_id == "PCOM 0203"
# assert course.max_capacity == 50
# assert course.term_id == "Term 1"
# assert course.transcript_hours == 15
# assert course.lecture_duration == 1.5

# # Test 5: Testing classroom class
# classroom = Classroom("11-533", 36, False)
# assert classroom.classroom_id == "11-533"
# assert classroom.capacity == 36
# assert classroom.lab_room == False

# # Test 6: Testing schedule class
# degree = Degree("BCOM", ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
# program = Program("PM", 100, ["PRDV 0201", "PRDV 0202", "PRDV 0203"])
# student = Student(1, "John Doe", degree, program)
# courses = [Course("PCOM 0203", 36, "Term 1", 15, 1.5), Course("SUPR 0751", 36, "Term 1", 7, 1.5), Course("PRDV 0201", 20, "Term 1", 21, 1.5), Course("PRDV 0202", 20, "Term 1", 14, 1.5)]
# classrooms = [Classroom("11-533", 36, False), Classroom("11-534", 36, False), Classroom("11-560", 24, False), Classroom("11-533", 24, False)]
# schedule = Schedule(student, degree, program, courses, classrooms)
# assert schedule.student == student
# assert schedule.degree == degree
# assert schedule.program == program
# assert schedule.courses == courses
# assert schedule.classrooms == classrooms
