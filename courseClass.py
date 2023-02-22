'''
Author: Victor Tadros
CMPT 395 X03L - Team: 3
Program Desc: Schedule core courses Monday/Wednesday, and program courses on Tuesday/Thursday. Program will validate if a time slot is free to schedule new course
'''

from Classes import *

class Schedule:
    def __init__(self, student, degree, program, courses, classrooms):
        self.student = student
        self.degree = degree
        self.program = program
        self.courses = courses
        self.classrooms = classrooms
    
   
    def display_schedule(self, classroom):
        print(f"\n{classroom.classroom_id}: ")
        for day in classroom.schedule:
            print(f"{day}: ")
            for course in classroom.schedule[day]:
                if course != None:
                    print(f"\t{course.course_id} starts at {course.lecture_start_time} and ends at {course.lecture_end_time}")
                else: print(f"\tNull")

    def schedule_core_courses(self):
        # loop through all classrooms in the instance
        for classroom in self.classrooms:
    
            # loop through days "Monday" and "Wednesday"
            for day in ["Monday", "Wednesday"]:
    
                # loop through core courses
                for key, values in self.degree.core_courses.items():
                    for course in values:
                    # check if the course can be scheduled on the current day and classroom
                        if course.lecture_duration in [1.5, 2]: 
                            if day == "Monday":
                                schedule_on_day = self.check_availability(course, day, classroom)
                                schedule_on_occurences = self.course_occurence(course, day, classroom)
                                if schedule_on_day and schedule_on_occurences:
                                    # schedule the course on the current day and classroom
                                    self.schedule_course(course, day, classroom)
                                else:
                                    print(f"Cannot schedule {course.course_id} on {day}")
                                
                            elif day == "Wednesday":
                                # If course has a duration of 1.5 or 2, check if it was scheduled on Monday
                                if course in classroom.schedule["Monday"]:
                                    schedule_on_day = self.check_availability(course, day, classroom)
                                    schedule_on_occurences = self.course_occurence(course, day, classroom)
                                    if schedule_on_day and schedule_on_occurences:
                                        # schedule the course on the current day and classroom
                                        self.schedule_course(course, day, classroom)
                                    else:
                                        print(f"Cannot schedule {course.course_id} on {day}")
                        else:
                            schedule_on_day = self.check_availability(course, day, classroom)
                            schedule_on_occurences = self.course_occurence(course, day, classroom)
                            if schedule_on_day and schedule_on_occurences:
                                # schedule the course on the current day and classroom
                                self.schedule_course(course, day, classroom)
                            else:
                                print(f"Cannot schedule {course.course_id} on {day}")


    def schedule_program_courses(self):
        # loop through all classrooms in the instance
        for classroom in self.classrooms:
            
            for day in ["Tuesday", "Thursday"]:
                    
                # loop through program courses
                for key, values in self.degree.core_courses.items():
                    for course in values:
                    # check if the course can be scheduled on the current day and classroom
                        if course.lecture_duration in [1.5, 2]: 
                            if day == "Tuesday":
                                schedule_on_day = self.check_availability(course, day, classroom)
                                schedule_on_occurences = self.course_occurence(course, day, classroom)
                                if schedule_on_day and schedule_on_occurences:
                                    # schedule the course on the current day and classroom
                                    self.schedule_course(course, day, classroom)
                                else:
                                    print(f"Cannot schedule {course.course_id} on {day}")
                                
                            elif day == "Thursday":
                                # If course has a duration of 1.5 or 2, check if it was scheduled on Monday
                                if course in classroom.schedule["Tuesday"]:
                                    schedule_on_day = self.check_availability(course, day, classroom)
                                    schedule_on_occurences = self.course_occurence(course, day, classroom)
                                    if schedule_on_day and schedule_on_occurences:
                                        # schedule the course on the current day and classroom
                                        self.schedule_course(course, day, classroom)
                                    else:
                                        print(f"Cannot schedule {course.course_id} on {day}")
                        else:
                            schedule_on_day = self.check_availability(course, day, classroom)
                            schedule_on_occurences = self.course_occurence(course, day, classroom)
                            if schedule_on_day and schedule_on_occurences:
                                # schedule the course on the current day and classroom
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
                    course.lecture_end_time = course.lecture_start_time + course.lecture_duration
        
                    # Check if new course start time overlaps with scheduled course end time
                    if course.lecture_start_time < scheduled_course_end_time:
                            return False
                    
                    # Check if the given day exists in the classroom's time slot
                        
                    elif classroom.lab_room == False:
                        if day in classroom.time_slot:
                            # Check if the start time is within the time slot
                            if course.lecture_start_time >= classroom.time_slot[day]["start"] and course.lecture_end_time <= classroom.time_slot[day]["end"]:
                                return True
                        
                    elif classroom.lab_room == True:
                        if day in classroom.time_slot_lab:
                            # Check if the start time is within the lab time slot
                            if course.lecture_start_time >= classroom.time_slot_lab[day]["start"] and course.lecture_end_time <= classroom.time_slot_lab[day]["end"]:
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
        
        # Check if the given day already has any courses scheduled
        if day in classroom.schedule:
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
                if scheduled_course == classroom.schedule[day][-1]:
                    
                    # Check if course is online to allow time before and after.
                    if course.online == True or scheduled_course.online == True:
                        # calculate the start/end time of new course
                        course.lecture_start_time = scheduled_course.lecture_end_time + .5
                        course.lecture_end_time = course.lecture_start_time + course.lecture_duration
                    else:    
                        # calculate the start/end time of new course
                        course.lecture_start_time = scheduled_course.lecture_end_time
                        course.lecture_end_time = course.lecture_start_time + course.lecture_duration
                    
                    # Check if the start time or end time of the new course overlaps with the scheduled course
                    if course.lecture_start_time < scheduled_course.lecture_end_time and course.lecture_end_time > scheduled_course.lecture_end_time:
                        print(f"Cannot schedule {course.course_id} on {day} as it overlaps with {scheduled_course.course_id}")
                        return False
                    
                    # Check if the end time of the course exceeds the end time of the time slot for the given day
                    elif course.lecture_end_time > classroom.time_slot[day]["end"] or course.lecture_end_time > classroom.time_slot_lab[day]["end"]:
                        print(f"Cannot schedule {course.course_id} on {day} as the end time exceeds the time slot end")
                        return False
            
            # If the new course does not overlap with any other courses, add it to the schedule for the given day
            classroom.schedule[day].append((course))
        else:
            # If no courses are scheduled for the given day, create a new entry in the schedule dictionary with the new course and classroom
            course.lecture_end_time = course.lecture_start_time + course.lecture_duration
            classroom.schedule[day] = [(course)]
        return True


    '''
    replace_course: will first check if there are any empty slots in schedule to add course.
                    If not, will check if course's transcript hours = 0 and swap with new course
    '''
    def replace_course(self, course, day, classroom):
         # Check if the given day already has any courses scheduled
        if day in classroom.schedule:
            #loop through each scheduled course of classroom schedule
            for scheduled_course in classroom.schedule[day]:
                
                #check if scheduled course has transcript hours = 0
                if scheduled_course.transcript_hours == 0:
                    #get index of scheduled course
                    ind = classroom.schedule[day].index(scheduled_course)
                    # if yes, compare lecture duration between old and new course and see if they can be swapped 
                    if scheduled_course.lecture_duration == course.lecture_duration:
                        course.lecture_start_time = scheduled_course.lecture_start_time
                        course.lecture_end_time = scheduled_course.lecture_end_time
                        print(f"{scheduled_course.course_id} is swapped with {course.course_id}")
                        classroom.schedule[day][ind] = course
                    
                    elif scheduled_course.lecture_duration > course.lecture_duration: 
                        course.lecture_start_time = scheduled_course.lecture_start_time
                        course.lecture_end_time = course.lecture_start_time + course.lecture_duration
                        print(f"{scheduled_course.course_id} is swapped with {course.course_id}")
                        classroom.schedule[day][ind] = course
                    
                    # if they cannot be swapped, replace old course with None
                    else:
                        classroom.schedule[day][ind] = None
                        print(f"{scheduled_course.course_id} has been removed from schedule")


    '''
    fill_empty_slot: searches for None in list and replaces with new course
    '''
    def fill_empty_spot(self, course, day, classroom):
         # Check if the given day already has any courses scheduled
        if day in classroom.schedule:
            #check if there is an empty slot in the classroom's schedule for the given day
            if None in classroom.schedule[day]:

                #find the index of the first empty slot in the classroom's schedule for the given day
                empty_slot_index = classroom.schedule[day].index(None)
                
                #find the index of the prev and next non-empty slot in the classroom's schedule for the given day
                prev_course_index = empty_slot_index - 1
                next_course_index = empty_slot_index + 1
                
                #get the prev and next non-empty course scheduled in the classroom's schedule for the given day
                prev_course = classroom.schedule[day][prev_course_index]
                next_course = classroom.schedule[day][next_course_index]

                #calculate the start time for the new course based on the end time of the prev course and staret time of next course
                if empty_slot_index == 0:
                    temp_start_time = 8
                    temp_end_time = course.lecture_start_time + course.lecture_duration
                else:    
                    temp_start_time = prev_course.lecture_end_time
                    temp_end_time = course.lecture_start_time + course.lecture_duration

                #check if end time is less the start time of next course
                if temp_end_time <= next_course.lecture_start_time:
                    course.lecture_start_time = temp_start_time
                    course.lecture_end_time = temp_end_time

                else:
                    print(f"Cannot schedule {course.course_id} as there is overlap with another course")
                    return False

                #insert the new course into the empty slot in the classroom's schedule for the given day
                classroom.schedule[day][empty_slot_index] = course
                print(f"Scheduled {course.course_id} on {day} at {course.lecture_start_time}")
                return True