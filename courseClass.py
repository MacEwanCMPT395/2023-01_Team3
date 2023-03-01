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
        self.scheduled_courses = []
        # self.unsched_courses = []   #unscheduled_courses waiting to be scheduled
    
   
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

                        if course.course_id not in self.scheduled_courses and classroom.class_type == course.course_type:

                            if course.lecture_duration in [1.5, 2]:
                                if day == "Monday":
                                    # check if the course can be scheduled on the current day and classroom
                                    schedule_on_day = self.check_availability(course, day, classroom)
                                    if schedule_on_day:
                                        # schedule the course on the current day and classroom
                                        self.schedule_course(course, day, classroom)
                                    
                                elif day == "Wednesday":
                                    # check if it was scheduled on Monday
                                    if course in classroom.schedule["Monday"]:
                                        schedule_on_day = self.check_availability(course, day, classroom)
                                        if schedule_on_day:
                                            # schedule the course on the current day and classroom
                                            self.schedule_course(course, day, classroom)
                                            self.scheduled_courses.append(course.course_id)

                            else:
                                schedule_on_day = self.check_availability(course, day, classroom)
                                if schedule_on_day:
                                    # schedule the course on the current day and classroom
                                    self.schedule_course(course, day, classroom)
                                    self.scheduled_courses.append(course.course_id)
                    
        # print(self.scheduled_courses)


    # def schedule_program_courses(self):
    #     # loop through all classrooms in the instance
    #     for classroom in self.classrooms:
            
    #         for day in ["Tuesday", "Thursday"]:
                    
    #             # loop through program courses
    #             for key, values in self.degree.core_courses.items():
    #                 for course in values:
    #                 # check if the course can be scheduled on the current day and classroom
    #                     if course.lecture_duration in [1.5, 2]: 
    #                         if day == "Tuesday":
    #                             schedule_on_day = self.check_availability(course, day, classroom)
    #                             schedule_on_occurences = self.course_occurence(course, day, self.classrooms)
    #                             if schedule_on_day and schedule_on_occurences:
    #                                 # schedule the course on the current day and classroom
    #                                 self.schedule_course(course, day, classroom)
    #                             else:
    #                                 print(f"Cannot schedule {course.course_id} on {day}")
                                
    #                         elif day == "Thursday":
    #                             # If course has a duration of 1.5 or 2, check if it was scheduled on Monday
    #                             if course in classroom.schedule["Tuesday"]:
    #                                 schedule_on_day = self.check_availability(course, day, classroom)
    #                                 schedule_on_occurences = self.course_occurence(course, day, self.classrooms)
    #                                 if schedule_on_day and schedule_on_occurences:
    #                                     # schedule the course on the current day and classroom
    #                                     self.schedule_course(course, day, classroom)
    #                                 else:
    #                                     print(f"Cannot schedule {course.course_id} on {day}")
    #                     else:
    #                         schedule_on_day = self.check_availability(course, day, classroom)
    #                         schedule_on_occurences = self.course_occurence(course, day, self.classrooms)
    #                         if schedule_on_day and schedule_on_occurences:
    #                             # schedule the course on the current day and classroom
    #                             self.schedule_course(course, day, classroom)
    #                         else:
    #                             print(f"Cannot schedule {course.course_id} on {day}")


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
                if scheduled_course == classroom.schedule[day][-1]:
        
                    # calculate the end time of the scheduled course
                    scheduled_course_end_time = scheduled_course.lecture_start_time + scheduled_course.lecture_duration
        
                    # calculate the start/end time of new course
                    course_start_time = scheduled_course_end_time
                    course_end_time = course_start_time + course.lecture_duration
        
                    # Check if new course start time overlaps with scheduled course end time
                    if course_start_time < scheduled_course_end_time:
                            return False
                    
                    # Check if the given day exists in the classroom's time slot
                        
                    elif classroom.class_type == 0:
                        if day in classroom.time_slot:
                            # Check if the start time is within the time slot
                            if course_start_time >= classroom.time_slot[day]["start"] and course_end_time <= classroom.time_slot[day]["end"]:
                                return True
                        
                    elif classroom.class_type == 1:
                        if day in classroom.time_slot_lab:
                            # Check if the start time is within the lab time slot
                            if course_start_time >= classroom.time_slot_lab[day]["start"] and course_end_time <= classroom.time_slot_lab[day]["end"]:
                                return True
    
                    # If the day is not in the time slot or the start time is not within the time slot, return False
                    return False
        
        # If the day does not exist in the schedule or there is no overlap, return True
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
                    if course.course_type == 2 or scheduled_course.course_type == 2:
                        # calculate the start/end time of new course
                        course.lecture_start_time = scheduled_course.lecture_end_time + .5
                        course.lecture_end_time = course.lecture_start_time + course.lecture_duration
                    else:    
                        # calculate the start/end time of new course
                        course.lecture_start_time = scheduled_course.lecture_end_time
                        course.lecture_end_time = course.lecture_start_time + course.lecture_duration

                    time_sched = self.timeslot_sched(scheduled_course, course, classroom, day)
                    if time_sched == False: return False
            
            # If the new course does not overlap with any other courses, add it to the schedule for the given day
            classroom.schedule[day].append((course))
        else:
            # If no courses are scheduled for the given day, create a new entry in the schedule dictionary with the new course and classroom
            course.lecture_end_time = course.lecture_start_time + course.lecture_duration
            classroom.schedule[day] = [(course)]
        return True
    
    
    ''' 
    Helper function for schedule_course
    Checks if lecture start and end time depending on if the classroom is or is not a lab
    '''
    def timeslot_sched(self, scheduled_course, course, classroom, day):
        # Check if the start time or end time of the new course overlaps with the scheduled course
        if course.lecture_start_time < scheduled_course.lecture_end_time and course.lecture_end_time > scheduled_course.lecture_end_time:
            print(f"Cannot schedule {course.course_id} on {day} as it overlaps with {scheduled_course.course_id}")
            return False
        
        if classroom.class_type == 1:
            if course.lecture_end_time > classroom.time_slot_lab[day]["end"]:
                print(f"Cannot schedule {course.course_id} on {day} as the end time exceeds the time slot end")
                return False
        else:
            # Check if the end time of the course exceeds the end time of the time slot for the given day
            if course.lecture_end_time > classroom.time_slot[day]["end"]:
                print(f"Cannot schedule {course.course_id} on {day} as the end time exceeds the time slot end")
                return False
            

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