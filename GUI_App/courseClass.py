'''
Author: Victor Tadros
CMPT 395 X03L - Team: 3
Program Desc: Schedule core courses Monday/Wednesday, and program courses on Tuesday/Thursday. Program will validate if a time slot is free to schedule new course
'''

from Classes import *

class Schedule:
    def __init__(self, student, degree, program, courses, classrooms, term):
        self.student = student
        self.degree = degree
        self.program = program
        self.courses = courses
        self.classrooms = classrooms
        self.term = term
    
   
    def display_classroom(self, term, classroom):
        for classrooms in term.term_sched[term.term_id]:
            for clsrm in classrooms:
                if clsrm.classroom_id == classroom.classroom_id:
                    self.display_schedule(clsrm)
                

    def display_schedule(self, classroom):
        class_schedule = ""
        class_schedule += f"\n\t{classroom.classroom_id}: "
        for day in classroom.schedule:
            class_schedule += f"\n\t\t{day}: "
            for course in classroom.schedule[day]:
                if course != None:
                    class_schedule += f"\n\t\t\t{course.course_id} starts at {course.lecture_start_time} and ends at {course.lecture_end_time}"
                else: 
                    class_schedule += f"\n\t\t\tNull"
        return class_schedule
    
    ##################### return the classes #####################

    def return_classroom(self, term, classroom):
        class_schedule = ""
        for classrooms in term.term_sched[term.term_id]:
            for clsrm in classrooms:
                if clsrm.classroom_id == classroom.classroom_id:
                    class_schedule += self.display_schedule(clsrm)
        return class_schedule
                

    def return_schedule(self, classroom):
        class_schedule = ""
        class_schedule += f"\n\t{classroom.classroom_id}: \n"
        for day in classroom.schedule:
            class_schedule += f"\t\t{day}: \n"
            for course in classroom.schedule[day]:
                if course != None:
                    class_schedule += f"\t\t\t{course.course_id} starts at {course.lecture_start_time} and ends at {course.lecture_end_time}\n"
                else: 
                    class_schedule += f"\t\t\tNull\n"
        return class_schedule


    #############################################################

    def display_term(self, terms):
        for term in terms:
            for id, sched in term.term_sched.items():
                print(f"\n\n{id}: ")
                for classrooms in sched:
                    for classroom in classrooms:
                        self.display_schedule(classroom)

    '''
    term_schedule: filter out courses to their specific terms, and then pass the list of courses to schedule_core_courses and schedule_program_courses
    '''
    def term_schedule(self, classrooms, terms):

        #iterate through terms
        for term in terms:
            
            term.classrooms = [classroom.copy() for classroom in classrooms]  # create a copy of classrooms for each term

            #loop through core courses
            for key, values in self.degree.core_courses.items():
                for course in values:

                    #organize courses to respective terms
                    if term.term_value == 1 and course.term == 1:
                        term.term_core_course.append(course)
                    elif term.term_value == 2 and course.term != 3:
                        term.term_core_course.append(course)
                    elif term.term_value == 3 and course.term != 1:
                        term.term_core_course.append(course)

            for key, values in self.program.program_courses.items():
                for course in values:

                    #organize courses to respective terms
                    if term.term_value == 1 and course.term == 1:
                        term.term_prog_course.append(course)
                    elif term.term_value == 2 and course.term != 3:
                        term.term_prog_course.append(course)
                    elif term.term_value == 3 and course.term != 1:
                        term.term_prog_course.append(course)

            self.schedule_core_courses(term.term_core_course, term.classrooms, term)
            self.schedule_program_courses(term.term_prog_course, term.classrooms, term)



    '''
    schedule_core_courses: will assign courses to monday and wednesday (once or twice a week depending on lecture_duration)
                           calls check_availability to see if a course can be scheduled within the general timeslot of a classroom with no conflicts
                           calls schedule_courses to assign the courses to a classroom.
    '''
    def schedule_core_courses(self, courses, classrooms, term):

        # loop through all classrooms in the instance
        for classroom in classrooms:
    
            # loop through days "Monday" and "Wednesday"
            for day in ["Monday", "Wednesday"]:
    
                # loop through core courses
                for course in courses:
                    
                    # check if course has already been scheduled and that course and classroom types are the same i.e. lab room = lab course
                    if course.course_id not in term.scheduled_courses and classroom.class_type == course.course_type:

                        if course.lecture_duration in [1.5, 2] and course.pre_req == None:
                            if day == "Monday":
                                # check if the course can be scheduled on the current day and classroom
                                schedule_on_day = self.check_availability(course, day, classroom)
                                if schedule_on_day:
                                    # schedule the course on the current day and classroom
                                    self.schedule_course(course, day, classroom)
                                else:
                                    term.assign_unsched(course)
                                
                            elif day == "Wednesday":
                                # check if it was scheduled on Monday
                                if course in classroom.schedule["Monday"]:
                                    schedule_on_day = self.check_availability(course, day, classroom)
                                    if schedule_on_day:
                                        # schedule the course on the current day and classroom
                                        self.schedule_course(course, day, classroom)
                                        term.scheduled_courses.append(course.course_id)

                        else:
                            schedule_on_day = self.check_availability(course, day, classroom)
                            if schedule_on_day:
                                # schedule the course on the current day and classroom
                                self.schedule_course(course, day, classroom)
                                term.scheduled_courses.append(course.course_id)
                            else:
                                term.assign_unsched(course)

        term.term_sched[term.term_id] = [(classrooms)]


        
    '''
    schedule_program_courses: will assign courses to tuesday and thusday (once or twice a week depending on lecture_duration) 
                              calls check_availability to see if a course can be scheduled within the general timeslot of a classroom with no conflicts
                              calls schedule_courses to assign the courses to a classroom.
                              
    '''
    def schedule_program_courses(self, courses, classrooms, term):
        # loop through all classrooms in the instance
        for classroom in classrooms:
    
            # loop through days "Tuesday" and "Thursday"
            for day in ["Tuesday", "Thursday"]:
    
                # loop through program courses
                for course in courses:

                    if course.course_id not in term.scheduled_courses and classroom.class_type == course.course_type:

                        if course.lecture_duration in [1.5, 2] and course.pre_req == None:
                            if day == "Tuesday":
                                # check if the course can be scheduled on the current day and classroom
                                schedule_on_day = self.check_availability(course, day, classroom)
                                if schedule_on_day:
                                    # schedule the course on the current day and classroom
                                    self.schedule_course(course, day, classroom)
                                else:
                                    term.assign_unsched(course)
                                    # term.unsched_courses.append(course)
                                
                            elif day == "Thursday":
                                # check if it was scheduled on Tuesday
                                if course in classroom.schedule["Tuesday"]:
                                    schedule_on_day = self.check_availability(course, day, classroom)
                                    if schedule_on_day:
                                        # schedule the course on the current day and classroom
                                        self.schedule_course(course, day, classroom)
                                        term.scheduled_courses.append(course.course_id)

                        else:
                            schedule_on_day = self.check_availability(course, day, classroom)
                            if schedule_on_day:
                                # schedule the course on the current day and classroom
                                self.schedule_course(course, day, classroom)
                                term.scheduled_courses.append(course.course_id)
                            else:
                                term.assign_unsched(course)
                                # term.unsched_courses.append(course)

        term.term_sched[term.term_id] = [(classrooms)]

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
                            # if course in self.program.program_courses["FS"]:
                            #     if course_start_time >= 5 and course_end_time <= classroom.time_slot_lab[day]["end"]:
                            #         return True
                            # else:
                                # Check if the start time is within the lab time slot
                            if course_start_time >= classroom.time_slot_lab[day]["start"] and course_end_time <= classroom.time_slot_lab[day]["end"]:#classroom.time_slot_lab[day]["end"]:
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
    def replace_course(self, term, classrooms):

        for classroom in classrooms:

            for day, values in classroom.schedule.items():
                for scheduled_course in values:
                
                    #check if scheduled course has transcript hours = 0
                    if scheduled_course.transcript_hours == 0:
                        #get index of scheduled course
                        ind = classroom.schedule[day].index(scheduled_course)

                        self.prereq_check(ind, scheduled_course, term, classroom, day)




    def prereq_check(self, ind, scheduled_course, term, classroom, day):
        
            #if we have unscheduled courses belonging to sam edepartment as scheduled_course
            if scheduled_course.department in term.unsched_courses:
                # for dep, courses in term.unsched_courses.items():
                    for course in term.unsched_courses[scheduled_course.department]:
                        if course.pre_req !=  None:
                            #check if course is not already scheduled and scheduled_course.course_id == course.pre_req
                            if course not in term.scheduled_courses and scheduled_course.course_id == course.pre_req:
                                # if yes, compare lecture duration between old and new course and see if they can be swapped
                                term.new_course_time(classroom, scheduled_course, term.unsched_courses[course.department], course, day, ind)
                                return
                        else:
                            if course not in term.scheduled_courses:
                                # if yes, compare lecture duration between old and new course and see if they can be swapped
                                term.new_course_time(classroom, scheduled_course, term.unsched_courses[course.department], course, day, ind)
                                return
                            
            #else, take unsecheduled course from any department
            else:
                for dep, courses in term.unsched_courses.items():
                    for course in courses:
                        if course.pre_req !=  None:
                            #check if course is not already scheduled and scheduled_course.course_id == course.pre_req
                            if course not in term.scheduled_courses and scheduled_course.course_id == course.pre_req:
                                term.new_course_time(classroom, scheduled_course, courses, course, day, ind)
                                return
                        else:
                            if course not in term.scheduled_courses:
                                term.new_course_time(classroom, scheduled_course, courses, course, day, ind)
                                return
                        
                            

    '''
    fill_empty_slot: searches for None in list and replaces with new course
    '''
    def fill_empty_spot(self, term, classrooms):

        for classroom in classrooms:
                
                for day, values in classroom.schedule.items():
                    #check if there is an empty slot in the classroom's schedule for the given day
                    if None in values:
                            
                            empty_slot_index, prev_course, next_course = self.find_null_index(classroom, day)

                            for dep, courses in term.unsched_courses.items():
                                for course in courses:
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
                            
    '''
    Helper function for fill_empty_slot:  
                        Will find the index of None in classroom schedule and find the courses scheduled before and after None
    '''                        
    def find_null_index(self, classroom, day):
        #find the index of the first empty slot in the classroom's schedule for the given day
        empty_slot_index = classroom.schedule[day].index(None)
        
        #find the index of the prev and next non-empty slot in the classroom's schedule for the given day
        prev_course_index = empty_slot_index - 1
        next_course_index = empty_slot_index + 1
        
        #get the prev and next non-empty course scheduled in the classroom's schedule for the given day
        prev_course = classroom.schedule[day][prev_course_index]
        next_course = classroom.schedule[day][next_course_index]

        return empty_slot_index, prev_course, next_course
