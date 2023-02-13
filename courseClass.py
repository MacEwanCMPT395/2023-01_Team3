'''
Author: Victor Tadros
CMPT 395 X03L - Team: 3
Program Desc: Schedule core courses Monday/Wednesday, and program courses on Tuesday/Thursday. Program will validate if a time slot is free to schedule new course
'''

class Student:
    def __init__(self, student_id, name, degree, program, term):
        self.student_id = student_id
        self.name = name
        self.degree = degree
        self.program = program
        self.term = term

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
        self.lecture_start_time = 8

class Classroom:
    def __init__(self, classroom_id, capacity, lab_room):
        self.classroom_id = classroom_id
        self.capacity = capacity
        self.lab_room = lab_room
        self.time_slot = {"Monday": {"start": 8, "end": 17},\
            "Tuesday": {"start": 8, "end": 17}, \
                "Wednesday": {"start": 8, "end": 17}, \
                    "Thursday": {"start": 8, "end": 17},}
        self.schedule = {}


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
    
    def display_schedule(self, classroom):
        for day in classroom.schedule:
            print(f"{day}: ")
            for course in classroom.schedule[day]:
                print(f"\t{course.course_id} starting at {course.lecture_start_time}")
                # print("\n")

    def schedule_courses(self):
        # loop through all classrooms in the instance
        for classroom in self.classrooms:
        
            # loop through days "Monday" and "Wednesday"
            for day in ["Monday", "Wednesday"]:
        
                # select courses that belong to degree
                core_courses = [course for course in self.degree.core_courses if self.degree.degree_id]
        
                # loop through core courses
                for course in core_courses:
        
                    # check if the course can be scheduled on the current day and classroom
                    schedule_on_day = self.check_availability(course, day, classroom)
                    schedule_on_occurences = self.course_occurence(course, day, classroom)
        
                    if schedule_on_day and schedule_on_occurences:
                        # schedule the course on the current day and classroom
                        self.schedule_course(course, day, classroom)
                    else:
                        print(f"Cannot schedule {course.course_id} on {day}")

            for day in ["Tuesday", "Thursday"]:
                # select courses that belong to program
                program_courses = [course for course in self.program.courses if self.program.program_id]
        
                for course in program_courses:
        
                    schedule_on_day = self.check_availability(course, day, classroom)
                    schedule_on_occurences = self.course_occurence(course, day, classroom)

                    if schedule_on_day and schedule_on_occurences:
                        self.schedule_course(course, day, classroom)
                    else:
                        print(f"Cannot schedule {course.course_id} on {day}")



    '''
    check_availability: will verify if a course is allowed to be placed in a classroom's schedule
                        function will return boolean; True = valid / False = invalid
    '''
    def check_availability(self, course, day, classroom):
        # Check if the given day already has any courses scheduled
        if day in classroom.schedule:
        
            # If it does, loop through each scheduled course of classroom schedule
            for scheduled_course in classroom.schedule[day]:
        
                # Find the last course that was scheduled in the classroom's schedule
                if scheduled_course.course_id == classroom.schedule[day][-1].course_id:
        
                    # calculate the end time of the scheduled course
                    scheduled_course_end_time = scheduled_course.lecture_start_time + scheduled_course.lecture_duration
        
                    # calculate the start/end time of new course
                    course.lecture_start_time = scheduled_course_end_time
                    lecture_end_time = course.lecture_start_time + course.lecture_duration
        
                    # Check if new course start time overlaps with scheduled course end time
                    if course.lecture_start_time < scheduled_course_end_time:
                            return False
                    
                    # Check if the given day exists in the classroom's time slot
                    elif day in classroom.time_slot:
        
                        # Check if the start time is within the time slot
                        if course.lecture_start_time >= classroom.time_slot[day]["start"] and lecture_end_time <= classroom.time_slot[day]["end"]:
                            return True
        
                    # If the day is not in the time slot or the start time is not within the time slot, return False
                    return False
        
        # If the day does not exist in the schedule or there is no overlap, return True
        return True


    '''
    course_occurence: will check number of times a course runs through a week.
                        - courses with lecture durations 1.5 and 2 = 2x
                        - else = 1x
    '''
    def course_occurence(self, course, day, classroom):
        # counter for courses that need to run twice/once a week
        occurences_two = 0
        occurences_one = 0
        
        #loop through each scheduled course of classroom schedule
        for scheduled_course in classroom.schedule[day]:
        
            #if course id = course id already scheduled, increment counters
            if scheduled_course.course_id == course.course_id and scheduled_course.lecture_duration != 3:
                occurences_two += 1
        
                # if counter requirments are satisfied, display error msg and return False
                if occurences_two == 2:
                    print(f"\nCannot schedule {course.course_id} as it has reached its maximum run time in a week\n")
                    return False
        
            elif scheduled_course.course_id == course.course_id and scheduled_course.lecture_duration == 3:
                occurences_one += 1
        
                # if counter requirments are satisfied, display error msg and return False
                if occurences_one == 1:
                    print(f"Cannot schedule {course.course_id} as it has reached its maximum run time in a week")
                    return False

        return True
        

    '''
    schedule_course: will verify if course can be placed in a classroom's schedule. 
                    If valid, will be added to the end of the schedule. 
                    Else, error message will be displayed and function will return False
    '''
    def schedule_course(self, course, day, classroom):
        # Check if the given day already has any courses scheduled
        if day in classroom.schedule:
            
            # If it does, loop through each scheduled course of classroom schedule
            for scheduled_course in classroom.schedule[day]:
            
                # Find the last course that was scheduled in the classroom's schedule
                if scheduled_course.course_id == classroom.schedule[day][-1].course_id:
                    
                    # calculate the end time of the scheduled course
                    scheduled_course_end_time = scheduled_course.lecture_start_time + scheduled_course.lecture_duration
                    
                    # calculate the start/end time of new course
                    course.lecture_start_time = scheduled_course_end_time
                    lecture_end_time = course.lecture_start_time + course.lecture_duration
                    
                    # Check if the start time or end time of the new course overlaps with the scheduled course
                    if course.lecture_start_time < scheduled_course_end_time and lecture_end_time > scheduled_course_end_time:
                        print(f"Cannot schedule {course.course_id} on {day} as it overlaps with {scheduled_course.course_id}")
                        return False
                    
                    # Check if the end time of the course exceeds the end time of the time slot for the given day
                    elif lecture_end_time > classroom.time_slot[day]["end"]:
                        print(f"Cannot schedule {course.course_id} on {day} as the end time exceeds the time slot end")
                        return False
            
            # If the new course does not overlap with any other courses, add it to the schedule for the given day
            classroom.schedule[day].append((course))
        else:
            # If no courses are scheduled for the given day, create a new entry in the schedule dictionary with the new course and classroom
            classroom.schedule[day] = [(course)]
        return True
