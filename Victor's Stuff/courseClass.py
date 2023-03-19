'''
Author: Victor Tadros
CMPT 395 X03L - Team: 3
Program Desc: Schedule core courses Monday/Wednesday, and program courses on Tuesday/Thursday. Program will validate if a time slot is free to schedule new course
'''

from Classes import *
import pandas as pd                 #pip install pandas
import numpy as np

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
        print(f"\n\t{classroom.classroom_id}: ")
        for day in classroom.schedule:
            print(f"\t\t{day}: ")
            for course in classroom.schedule[day]:
                if course != None:
                    print(f"\t\t\t{course.course_id} starts at {course.lecture_start_time} and ends at {course.lecture_end_time}")
                else: print(f"\t\t\tNull")

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

            #create copies of all courses for each term (for distinct times)
            term.core_courses = Course.copy(self, self.degree.core_courses)
            term.program_courses = Course.copy(self, self.program.program_courses)

            #loop through core courses
            for core in term.core_courses:

                    #organize courses to respective terms
                    if term.term_value == 1 and core.term == 1:
                        term.term_core_course.append(core)
                    elif term.term_value == 2 and core.term != 3:
                        term.term_core_course.append(core)
                    elif term.term_value == 3 and core.term != 1:
                        term.term_core_course.append(core)

            for prog in term.program_courses:

                    #organize courses to respective terms
                    if term.term_value == 1 and prog.term == 1:
                        term.term_prog_course.append(prog)
                    elif term.term_value == 2 and prog.term != 3:
                        term.term_prog_course.append(prog)
                    elif term.term_value == 3 and prog.term != 1:
                        term.term_prog_course.append(prog)

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

                        if course.lecture_duration in [1.5, 2]:
                            if day == "Monday":
                                # check if the course can be scheduled on the current day and classroom
                                schedule_on_day = self.check_availability(course, day, classroom)
                                if schedule_on_day and course.pre_req == None:
                                    # schedule the course on the current day and classroom
                                    self.schedule_course(course, day, classroom, term)
                                else:
                                    term.assign_unsched(course)
                                
                            elif day == "Wednesday":
                                # check if it was scheduled on Monday
                                if course in classroom.schedule["Monday"]:
                                    schedule_on_day = self.check_availability(course, day, classroom)
                                    if schedule_on_day:
                                        # schedule the course on the current day and classroom
                                        self.schedule_course(course, day, classroom, term)
                                        term.scheduled_courses.append(course.course_id)

                        else:
                            schedule_on_day = self.check_availability(course, day, classroom)
                            if schedule_on_day and course.pre_req == None:
                                # schedule the course on the current day and classroom
                                self.schedule_course(course, day, classroom, term)
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
                                if schedule_on_day and course.pre_req == None:
                                    # schedule the course on the current day and classroom
                                    self.schedule_course(course, day, classroom, term)
                                else:
                                    term.assign_unsched(course)
                                    # term.unsched_courses.append(course)
                                
                            elif day == "Thursday":
                                # check if it was scheduled on Tuesday
                                if course in classroom.schedule["Tuesday"]:
                                    schedule_on_day = self.check_availability(course, day, classroom)
                                    if schedule_on_day:
                                        # schedule the course on the current day and classroom
                                        self.schedule_course(course, day, classroom, term)
                                        term.scheduled_courses.append(course.course_id)

                        else:
                            schedule_on_day = self.check_availability(course, day, classroom)
                            if schedule_on_day and course.pre_req == None:
                                # schedule the course on the current day and classroom
                                self.schedule_course(course, day, classroom, term)
                                term.scheduled_courses.append(course.course_id)
                            else:
                                term.assign_unsched(course)
                                # term.unsched_courses.append(course)
        
        # term.display_au()
        term.term_sched[term.term_id] = [(classrooms)]


    '''
    check_availability: will verify if a course is allowed to be placed in a classroom's schedule
                        function will return boolean; True = valid / False = invalid

            [[0] ... CRS(strt = 16, end = 18), CRS(strt = 18, end = 20)] **start from index[-1]
    '''
    def check_availability(self, course, day, classroom):
        # Check if the given day already has any courses scheduled
        if day in classroom.schedule:
        
            # If it does, loop through each scheduled course of classroom schedule
            for scheduled_course in classroom.schedule[day]:
        
                # Find the last course that was scheduled in the classroom's schedule
                if scheduled_course == classroom.schedule[day][0]:
        
                    # calculate the end time of the scheduled course
                    scheduled_course_start_time = scheduled_course.lecture_end_time - scheduled_course.lecture_duration
        
                    # calculate the start/end time of new course
                    course_end_time = scheduled_course_start_time
                    course_start_time = course_end_time - course.lecture_duration
        
                    # Check if new course start time overlaps with scheduled course end time
                    if course_end_time > scheduled_course_start_time:
                            return False
                    
                    # Check if the given day exists in the classroom's time slot
                        
                    if classroom.class_type == 0:
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
    def schedule_course(self, course, day, classroom, term):
        # Check if the given day already has any courses scheduled
        if day in classroom.schedule:
            
            # If it does, loop through each scheduled course of classroom schedule
            for scheduled_course in classroom.schedule[day]:
            
                # Find the last course that was scheduled in the classroom's schedule
                if scheduled_course == classroom.schedule[day][0]:
                    
                    # check if course department is FS
                    if course.department != "FS":
                        # calculate the start/end time of new course, must be scheduled away from the end of day 
                        if scheduled_course.lecture_start_time >= 16:
                            course.lecture_end_time = 16
                            course.lecture_start_time = course.lecture_end_time - course.lecture_duration
                        else:
                            course.lecture_end_time = scheduled_course.lecture_start_time
                            course.lecture_start_time = course.lecture_end_time - course.lecture_duration
                        
                        # Check if course is online to allow time before and after.
                        if course.course_type == 2 or scheduled_course.course_type == 2:
                            # calculate the start/end time of new course
                            course.lecture_end_time = scheduled_course.lecture_start_time - .5
                            course.lecture_start_time = course.lecture_end_time - course.lecture_duration
                    
                    else:
                        # calculate the start/end time of new course
                        course.lecture_end_time = scheduled_course.lecture_start_time
                        course.lecture_start_time = course.lecture_end_time - course.lecture_duration

                    time_sched = self.timeslot_sched(term, scheduled_course, course, classroom, day)
                    if time_sched == False: return False

            '''
            Once time_sched approves of course time, we will call track_times
            After being added to term.track, we wil then verify using 
            '''
            # track = self.track_times(course, term)
            # if track == True:
                # If the new course does not overlap with any other courses, add it to the schedule for the given day
            classroom.schedule[day].insert(0, (course))
        else:

            if course.department != "FS":
                # If no courses are scheduled for the given day, create a new entry in the schedule dictionary with the new course and classroom
                course.lecture_start_time = course.lecture_end_time - course.lecture_duration
                # track = self.track_times(course, term)
                # if track == True:
                classroom.schedule[day] = [(course)]
            else: 
                # If no courses are scheduled for the given day, create a new entry in the schedule dictionary with the new course and classroom
                course.lecture_end_time = 20
                course.lecture_start_time = course.lecture_end_time - course.lecture_duration
                
                # track = self.track_times(course, term)
                # if track == True:
                classroom.schedule[day] = [(course)]
            
        return True
    
    
    ''' 
    Helper function for schedule_course
    Checks if lecture start and end time depending on if the classroom is or is not a lab
    '''
    def timeslot_sched(self, term, scheduled_course, course, classroom, day):
        # Check if the start time or end time of the new course overlaps with the scheduled course
        if course.lecture_start_time < scheduled_course.lecture_end_time and course.lecture_end_time > scheduled_course.lecture_end_time:
            print(f"Cannot schedule {course.course_id} on {day} as it overlaps with {scheduled_course.course_id}")
            return False
        
        if classroom.class_type == 1:
            if course.department != "FS":
                if day in ["Tuesday", "Thursday"]:
                    # Check if the start time is within the lab time slot
                    if course.lecture_end_time > 16:
                        return False
                else:
                    if course.lecture_start_time < classroom.time_slot_lab[day]["start"]:
                        print(f"Cannot schedule {course.course_id} on {day} as the end time exceeds the time slot end")
                        return False
            else:
                # Schedule for "FS" department from 16 until time_slot["end"]
                    if course.lecture_start_time < 16:
                        if course.department not in term.unsched_courses:
                            term.unsched_courses[course.department] = [course]
                        else:
                            term.unsched_courses[course.department].append(course)
                        # print(f"Cannot schedule {course.course_id} on {day} as the end time exceeds the time slot end")
                        return False
        
        else:
            # Check if the end time of the course exceeds the end time of the time slot for the given day
            if course.lecture_start_time < classroom.time_slot[day]["start"]:
                print(f"Cannot schedule {course.course_id} on {day} as the end time exceeds the time slot end")
                return False
            

    '''
    Ok, so we need to be able to limit the number of courses from each department scheduled in a term at once.
    If we dont then courses belonging to the same department will run at the same time. Making it impossible for students to attend both classes.
    We need to keep track of the terms that include more than one specific courses (Ex. CMSK 101 (term 1), CMSK 103 (term 2)). SO not only do we need to consider the time, 
    but also the term since term 1 students will take courses for term 1 and term 2 students will take courses for term 2. (Not need for Term 1)

    The way I though about going about this is to create a dictionary in class Term that will keep track of the start and end times of each course belonging to the same department.
    It would be a something like this: 
                                        {"PCOM" : [[17, 15.5], 
                                                   [15.5, 14],
                                                    ...],
                                         "BCOM" : [[17, 15],
                                                   [15, 13.5],
                                                   ...],
                                          ...          
                                        }

    we would also have a condition in play that will track the term specific courses so that we dont limit the courses being scheduled at once
    (Eg. Only have term 1 courses scheduled and not term 2 courses)
    OR
    we could include the term of each course in the dictionary that trackes the time of each course:
                                        {"PCOM" : {Term 1: [[17, 15.5], 
                                                   [15.5, 14],
                                                    ...]},
                                                  {Term 2: [[17, 15],
                                                            [15, 13.5],
                                                            ...]}
                                        }
    Will most likely use this, more organized

    I think its best to make a new function and then have it called in schedule_course, that way the parameters can be passed directly in the moment of scheduling
    function will return boolean just like check_availability.
    '''
    
    
    
    '''
    verify_times: will check to see if there is any overlap with other course belonging to the same course and term.
    parameters: course; use new calculated start and end times of course to check if overlap occurs 
                term; uses track attribute, a distinct dictionary for each term taht will track times of each scheduled course
    '''
    def verify_times(self, course, term):
        times = term.track[course.department][course.term]
        for time in times:
            if course.lecture_duration in [1.5, 2] and course.count != 2:
                if course.lecture_start_time == time[1] or course.lecture_end_time == time[0]:
                    return False
                elif time[1] < course.lecture_start_time < time[0] or time[1] < course.lecture_end_time < time[0]:
                    return False
                else:
                    course.count += 1
            elif course.lecture_duration not in [1.5, 2] and course != 1:
                if course.lecture_start_time == time[1] or course.lecture_end_time == time[0]:
                    return False
                elif time[1] < course.lecture_start_time < time[0] or time[1] < course.lecture_end_time < time[0]:
                    return False
                else:
                    course.count += 1
            elif (course.lecture_duration in [1.5, 2] and course.count != 2) or (course.lecture_duration not in [1.5, 2] and course != 1):
                return False
        print(f"check {course.course_id} ***, count {course.count} ")
        
        return True

    
    
    '''
    track_times: will add department, course term, and course start/end times in a nested dictionary format, See above.
    parameters: course; course object where ea can grab the start, end, and term of course
                term; uses track attribute, a distinct dictionary for each term, that we will later use to check any conflicts between courses with like departments across all classrooms
    '''
    def track_times(self, course, term):
        if course.department not in term.track:
            term.track[course.department] = {}
            if course.term not in term.track[course.department]:
                # print(f"check {course.course_id}, count {course.count}")
                term.track[course.department][course.term] = [[course.lecture_end_time, course.lecture_start_time]]
            else: 
                if self.verify_times(course, term) == True:
                    term.track[course.department][course.term].append([course.lecture_end_time, course.lecture_start_time])
                else:
                    if course.department not in term.unsched_courses:
                        term.unsched_courses[course.department] = [(course)]
                    else:
                        term.unsched_courses[course.department].append((course))
                    return False
        else:
            if course.term not in term.track[course.department]:
                # print(f"check {course.course_id} ***, count {course.count} ")
                term.track[course.department][course.term] = [[course.lecture_end_time, course.lecture_start_time]]
            else:
                if self.verify_times(course, term) == True: 
                    term.track[course.department][course.term].append([course.lecture_end_time, course.lecture_start_time])
                else:
                    if course.department not in term.unsched_courses:
                        term.unsched_courses[course.department] = [(course)]
                    else:
                        term.unsched_courses[course.department].append((course))
                    return False
        
        return True


    
    
    '''
    replace_course: will first check if there are any empty slots in schedule to add course.
                    If not, will check if course's transcript hours = 0 and swap with new course
    '''
    def replace_course(self, term, classrooms):
        
        for classroom in classrooms:
        
            for day, values in classroom.schedule.items():
        
                for scheduled_course in values:
        
                    # Check if scheduled course has transcript hours = 0
                    if scheduled_course.transcript_hours == 0 and scheduled_course.lecture_duration not in [1.5, 2]:
                        # Get index of scheduled course
                        scheduled_index = {scheduled_course: {day: classroom.schedule[day].index(scheduled_course)}}
                        self.prereq_check(scheduled_index, term, classroom)
        
                    elif scheduled_course.transcript_hours == 0 and scheduled_course.lecture_duration in [1.5, 2]:
                        scheduled_index = {scheduled_course: {day: classroom.schedule[day].index(scheduled_course)}}
        
                        # Iterate over the remaining days in the schedule to find the second occurrence of the course
                        for other_day, other_values in classroom.schedule.items():
        
                            if other_day != day and scheduled_course in other_values:
                                scheduled_index[scheduled_course][other_day] = other_values.index(scheduled_course)
                                break
        
                        self.prereq_check(scheduled_index, term, classroom)



    '''
    prereq_check: checks to see if a course has a prereq, if prereq is None then pass as parameter to new_course_time
    '''

    def prereq_check(self, ind, term, classroom):
        valid_courses = []
        # print("IND = ", ind)

        for scheduled_course, occurences in ind.items():
            #if we have unscheduled courses belonging to same department as scheduled_course
            if scheduled_course.department in term.unsched_courses:
                for course in term.unsched_courses[scheduled_course.department]:
                    if course.pre_req !=  None:
                        #check if course is not already scheduled and scheduled_course.course_id = course.pre_req
                        if course not in term.scheduled_courses and scheduled_course.course_id == course.pre_req:
                            # append the valid course to the list
                            valid_courses.append(course)
                    else:
                        if course not in term.scheduled_courses:
                            # append the valid course to the list
                            valid_courses.append(course)
                                    
            #else, take unscheduled course from any department
            else:
                for dep, courses in term.unsched_courses.items():
                    for course in courses:
                        if course.pre_req !=  None:
                            #check if course is not already scheduled and scheduled_course.course_id == course.pre_req
                            if course not in term.scheduled_courses and scheduled_course.course_id == course.pre_req:
                                print("#")
                                # append the valid course to the list
                                valid_courses.append(course)
                        else:
                            if course not in term.scheduled_courses:
                                # append the valid course to the list
                                valid_courses.append(course)
            
            # pass all the valid courses to the new_course_time method\
            term.new_course_time(classroom, term.unsched_courses, valid_courses, ind)

                        
                            

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
    
def read_csv(fileName):
    # Function to read csv file and store in class structures for scheduler.
    df = pd.read_csv(fileName)
    df = df.replace(np.nan, None) 
    courses = [] # update with created class objects as scanned
    #courseIDs = [] # list for program initialization after scanning whole csv
    degree = Degree()
    program = Program(150, '') # '' is only so initialization doesn't fail will fill courses after reading csv
    degree.core_courses["PCOM"] = [] # resetting hard coded values
    degree.core_courses["PCOM"] = [] # resetting hard coded values

    for i in range(len(df)):
        # df.values returns an array which is why I must surround it with brackets and then call for index 0 each time I append a courseID same goes for the courses creation
        #courseIDs.append((df.values[[i],[1]])[0])
        #print((df.values[[i],[0]])[0])
        if (df.values[[i],[0]])[0] == 'PCOM':
            degree.core_courses["PCOM"].append(Course((df.values[[i],[1]])[0], (df.values[[i],[0]])[0], (df.values[[i],[5]])[0], 70, (df.values[[i],[3]])[0], (df.values[[i],[6]])[0], (df.values[[i],[7]])[0], (df.values[[i],[4]])[0]))
        
        if (df.values[[i],[0]])[0] == 'BCOM':
            degree.core_courses["BCOM"].append(Course((df.values[[i],[1]])[0], (df.values[[i],[0]])[0], (df.values[[i],[5]])[0], 70, (df.values[[i],[3]])[0], (df.values[[i],[6]])[0], (df.values[[i],[7]])[0], (df.values[[i],[4]])[0]))
        
        if (df.values[[i],[0]])[0] == 'PM':
            program.program_courses["PM"].append(Course((df.values[[i],[1]])[0], (df.values[[i],[0]])[0], (df.values[[i],[5]])[0], 70, (df.values[[i],[3]])[0], (df.values[[i],[6]])[0], (df.values[[i],[7]])[0], (df.values[[i],[4]])[0]))
        
        if (df.values[[i],[0]])[0] == 'BA':
            program.program_courses["BA"].append(Course((df.values[[i],[1]])[0], (df.values[[i],[0]])[0], (df.values[[i],[5]])[0], 70, (df.values[[i],[3]])[0], (df.values[[i],[6]])[0], (df.values[[i],[7]])[0], (df.values[[i],[4]])[0]))
        
        if (df.values[[i],[0]])[0] == 'GLM':
            program.program_courses["GLM"].append(Course((df.values[[i],[1]])[0], (df.values[[i],[0]])[0], (df.values[[i],[5]])[0], 70, (df.values[[i],[3]])[0], (df.values[[i],[6]])[0], (df.values[[i],[7]])[0], (df.values[[i],[4]])[0]))
        
        if (df.values[[i],[0]])[0] == 'FS':
            program.program_courses["FS"].append(Course((df.values[[i],[1]])[0], (df.values[[i],[0]])[0], (df.values[[i],[5]])[0], 70, (df.values[[i],[3]])[0], (df.values[[i],[6]])[0], (df.values[[i],[7]])[0], (df.values[[i],[4]])[0]))
        
        if (df.values[[i],[0]])[0] == 'DXD':
            program.program_courses["DXD"].append(Course((df.values[[i],[1]])[0], (df.values[[i],[0]])[0], (df.values[[i],[5]])[0], 70, (df.values[[i],[3]])[0], (df.values[[i],[6]])[0], (df.values[[i],[7]])[0], (df.values[[i],[4]])[0]))
        
        if (df.values[[i],[0]])[0] == 'BK':
            program.program_courses["BK"].append(Course((df.values[[i],[1]])[0], (df.values[[i],[0]])[0], (df.values[[i],[5]])[0], 70, (df.values[[i],[3]])[0], (df.values[[i],[6]])[0], (df.values[[i],[7]])[0], (df.values[[i],[4]])[0]))
        
        courses.append(Course((df.values[[i],[1]])[0], (df.values[[i],[0]])[0], (df.values[[i],[5]])[0], 70, (df.values[[i],[3]])[0], (df.values[[i],[6]])[0], (df.values[[i],[7]])[0], (df.values[[i],[4]])[0]))
        # Note 70 is the max capacity we dont have a field for this so I just chose 70 for now
    program.courses = courses
    for i in range(len(degree.core_courses["PCOM"])):
        print(degree.core_courses["PCOM"][i].course_id)
    return courses, program

