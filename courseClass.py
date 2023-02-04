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

class Classroom:
    def __init__(self, classroom_id, capacity, lab_room):
        self.classroom_id = classroom_id
        self.capacity = capacity
        self.lab_room = lab_room


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
        self.lecture_start_time = 8

    # def generate_schedule(self):
    #     schedule = []
    #     for course in self.courses:
    #         for classroom in self.classrooms:
    #             if classroom.capacity >= course.max_capacity:
    #                 schedule.append((course, classroom))
    #                 break
    #     return schedule

    def schedule_courses(self):
        # lecture_start_time = 8
        # loop through all classrooms in the instance
        for classroom in self.classrooms:
            # loop through days "Monday" and "Wednesday"
            for day in ["Monday", "Wednesday"]:
                # select courses that belong to degree
                core_courses = [course for course in self.degree.core_courses \
                    if self.degree.degree_id == "PCOM" or self.degree.degree_id == "BCOM"]
                # loop through core courses
                for course in core_courses:
                    # check if the course can be scheduled on the current day and classroom
                    schedule_on_day = self.check_availability(day, classroom, self.lecture_start_time)
                    if schedule_on_day:
                        # check if the time slot for the course is available on the current day and classroom
                        if self.check_time_slot(day, classroom, self.lecture_start_time):
                            # schedule the course on the current day and classroom
                            self.schedule_course(course, day, classroom)
                            self.lecture_start_time = course.lecture_duration + self.lecture_start_time
                        else:
                            print(f"Cannot schedule {course.course_id} on {day}")

            for day in ["Tuesday", "Thursday"]:
                # select courses that belong to program
                program_courses = [course for course in self.program.courses]
                for course in program_courses:
                    schedule_on_day = self.check_availability(day, classroom, self.lecture_start_time)
                    if schedule_on_day:
                        if self.check_time_slot(day, classroom, self.lecture_start_time):
                            self.schedule_course(course, day, classroom)
                            self.lecture_start_time = course.lecture_duration + self.lecture_start_time
                        else:
                            print(f"Cannot schedule {course.course_id} on {day}")



    def check_availability(self, day, classroom, lecture_start_time):
    # Check if the given day exists in the schedule
        if day in self.schedule:
            # Iterate over all courses scheduled for the day
            for scheduled_course, scheduled_classroom in self.schedule[day]:
                # Check if the scheduled course is in the same classroom as the given classroom
                if scheduled_classroom == classroom:
                    # Calculate the end time of the scheduled course
                    end_time = lecture_start_time + scheduled_course.lecture_duration
                    # Check if the lecture start time is within the time slot and the end time is within the time slot
                    if lecture_start_time <= end_time <= self.time_slot[day]["end"]:
                        return False
        # If the day does not exist in the schedule or there is no overlap, return True
        return True


    def check_time_slot(self, day, classroom, lecture_start_time): 
        # Check if the day is already in the schedule
        if day in self.schedule:
            # Iterate through each scheduled course for the given day
            for scheduled_course, scheduled_classroom in self.schedule[day]:
                # Check if the same classroom is scheduled
                if scheduled_classroom == classroom:
                    # Calculate the end time of the scheduled course
                    end_time = lecture_start_time + scheduled_course.lecture_duration
                    # Check if the scheduled course overlaps with the new course
                    if lecture_start_time < end_time and end_time <= self.time_slot[day]["end"]:
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
