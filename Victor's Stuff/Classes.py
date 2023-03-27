'''
Author: Victor Tadros
CMPT 395 X03L - Team: 3
Purpose: Build classes for students, degree, program, course, and classroom
'''

class Student:
    def __init__(self, student_id, name, degree, program, term):
        self.student_id = student_id
        self.name = name
        self.degree = degree
        self.program = program
        self.term = term


class Course:
    def __init__(self, course_id, department, pre_req, max_capacity, term, transcript_hours, lecture_duration, course_type, lecture_start_time = 16, lecture_end_time = 17):
        self.course_id = course_id
        self.department = department
        self.pre_req = pre_req
        self.max_capacity = max_capacity
        self.term = term
        self.transcript_hours = transcript_hours
        self.lecture_duration = lecture_duration
        self.lecture_start_time = lecture_start_time
        self.lecture_end_time = lecture_end_time
        self.course_type = course_type
        # self.count = 0
        # self.sections = []

    '''
    copy: make identical copy of courses so each course has a distinct start and end time.
    '''
    def copy(self, courses):
        copy_courses = []
        for id, crs in courses.items():
            for course in crs:
                copy_courses.append(Course(course.course_id, course.department, course.pre_req, course.max_capacity, course.term, course.transcript_hours, course.lecture_duration, course.course_type))
        return copy_courses


    # class Section:
    #     def __init__(self):
    #         self.section_id = f"{Course.course_id}-{Course.term}-{1 + len(Course.sections)}"
    #         self.lecture_start_time = 8
    #         self.lecture_end_time = 9
    #         self.lecture_duration = self.__class__.lecture_duration
            

    # def add_section(self):
    #     section = Course.Section()
    #     self.sections.append(section)


class Degree:
    def __init__(self):
        self.degree_id = ["PCOM", "BCOM"]
        self.core_courses = {
                "PCOM": [Course("PCOM 0101", "PCOM", None, 70, 1, 35, 1.5, 0),
                        Course("PCOM 0105", "PCOM", None, 70, 1, 35, 1.5, 0),
                        Course("PCOM 0107", "PCOM", None, 70, 1, 18, 1.5, 1),
                        Course("CMSK 0233", "PCOM", None, 70, 1, 7, 1.5, 1), 
                        Course("CMSK 0235", "PCOM", None, 70, 1, 6, 1.5, 1),
                        Course("PCOM 0102", "PCOM", None, 70, 2, 35, 1.5, 0),
                        Course("PCOM 0201", "PCOM", None, 70, 2, 35, 1.5, 0),
                        Course("PCOM 0108", "PCOM", None, 70, 2, 18, 1.5, 1), 
                        Course("PCOM 0202", "PCOM", None, 70, 3, 33, 1.5, 0),
                        Course("PCOM 0103", "PCOM", None, 70, 3, 35, 1.5, 0),
                        Course("PCOM 0109", "PCOM", None, 70, 3, 14, 2, 3),
                        #PCOM 0109 runs in a classroom and lab?
                        ], 
                "BCOM": [Course("PCOM 0203", "BCOM", None, 70, 1, 15, 1.5, 0),
                        Course("SUPR 0751", "BCOM", None, 70, 1, 7, 2, 0),
                        Course("PCOM 0204", "BCOM", None, 70, 1, 35, 1.5, 0),
                        Course("CMSK 0237", "BCOM", None, 70, 1, 12, 1.5, 2),
                        Course("SUPR 0837", "BCOM", None, 70, 1, 7, 2, 0),
                        Course("SUPR 0841", "BCOM", None, 70, 1, 35, 2, 0),
                        Course("SUPR 0821", "BCOM", None, 70, 2, 7, 2, 0),
                        Course("SUPR 0822", "BCOM", None, 70, 2, 7, 2, 0),
                        Course("SUPR 0718", "BCOM", None, 70, 2, 7, 2, 0),
                        Course("SUPR 0836", "BCOM", None, 70, 2, 7, 2, 0),
                        Course("AVDM 0199", "BCOM", None, 70, 2, 3, 1.5, 2),
                        Course("PCOM 0106", "BCOM", None, 70, 2, 35, 2, 0), #schedule for 17 sessions
                        Course("PCOM 0205", "BCOM", None, 70, 3, 30, 3, 0),
                        Course("PCOM TBD", "BCOM", None, 70, 3, 21, 1.5, 0),
                        Course("PCOM 0207", "BCOM", None, 70, 3, 6, 2, 0),
                        Course("SUPR 0863", "BCOM", None, 70, 3, 7, 2, 0),
                        Course("PCOM 0206", "BCOM", None, 70, 3, 6, 3, 0),
                        Course("AVDM 0260", "BCOM", None, 70, 3, 6, 1.5, 2) #schedule after all classes are done, end of the term
                        ]}



class Program:
    def __init__(self, max_capacity, courses):
        self.program_id = ["PM", "BA", "GLM", "FS", "DXD", "BK"]
        self.program_courses = {"PM" : [Course("PRDV 0201", "PM", None, 70, 1, 21, 1.5, 0),
                                        Course("PRDV 0202", "PM", None, 70, 1, 14, 1.5, 0),
                                        Course("PRDV 0203", "PM", None, 70, 1, 21, 1.5, 0),
                                        Course("PRDV 0204", "PM", None, 70, 2, 14, 1.5, 0),
                                        Course("PRDV 0205", "PM", None, 70, 2, 21, 1.5, 0),
                                        Course("PCOM 0103", "PM", None, 70, 2, 21, 1.5, 0),
                                        Course("PRDV 0206", "PM", None, 70, 2, 14, 1.5, 0),
                                        Course("PRDV 0207", "PM", None, 70, 3, 14, 1.5, 0),
                                        Course("PRDV 0131", "PM", None, 70, 3, 39, 1.5, 0)],

                                "BA" : [Course("PRDV 0640", "BA", None, 70, 1, 21, 1.5, 0),
                                        Course("PRDV 0652", "BA", None, 70, 1, 14, 1.5, 0),
                                        Course("PRDV 0653", "BA", None, 70, 1, 21, 1.5, 0),
                                        Course("PRDV 0642", "BA", None, 70, 1, 14, 1.5, 0),
                                        Course("PRDV 0644", "BA", None, 70, 2, 21, 1.5, 0),
                                        Course("PRDV 0648", "BA", None, 70, 2, 14, 1.5, 0),
                                        Course("PCOM 0140", "BA", None, 70, 2, 35, 1.5, 0),
                                        Course("PRDV 0646", "BA", None, 70, 3, 14, 1.5, 0),
                                        Course("PRDV 0141", "BA", None, 70, 3, 39, 1.5, 0)],
                                        
                                "GLM" : [Course("SCMT 0501", "GLM", None, 70, 1, 21, 1.5, 0),
                                        Course("SCMT 0502", "GLM", None, 70, 1, 21, 1.5, 0),
                                        Course("PRDV 0304", "GLM", None, 70, 1, 15, 1.5, 0),
                                        Course("SCMT 0503", "GLM", None, 70, 2, 15, 1.5, 0),
                                        Course("SCMT 0504", "GLM", None, 70, 2, 21, 1.5, 0),
                                        Course("SCMT 0505", "GLM", None, 70, 3, 21, 1.5, 0),
                                        Course("PCOM 0151", "GLM", None, 70, 3, 39, 1.5, 0)],
                                
                                "FS" : [Course("CMSK 0150", "FS", None, 70, 1, 16, 2, 1),
                                        Course("CMSK 0151", "FS", None, 70, 1, 16, 2, 1),
                                        Course("CMSK 0157", "FS", None, 70, 1, 16, 2, 1),
                                        Course("CMSK 0154", "FS", None, 70, 1, 16, 2, 1),
                                        Course("CMSK 0152", "FS", "CMSK 0151", 16, 1, 16, 2, 1),
                                        Course("PCOM 0160", "FS", None, 70, 3, 50, 2, 1),
                                        Course("CMSK 0153", "FS", None, 70, 2, 18, 2, 1),
                                        Course("CMSK 0200", "FS", None, 70, 2, 16, 2, 1),
                                        Course("CMSK 0201", "FS", "CMSK 0200", 70, 2, 18, 2, 1),
                                        Course("CMSK 0203", "FS", None, 70, 2, 16, 2, 1),
                                        Course("CMSK 0202", "FS", None, 70, 2, 18, 2, 1)],

                                "DXD" : [Course("AVDM 0165", "DXD", None, 70, 1, 18, 1.5, 1),
                                         Course("DXDI 0101", "DXD", None, 70, 1, 24, 1.5, 1),
                                         Course("DXDI 0102", "DXD", "DXDI 0101", 70, 1, 24, 1.5, 1),
                                         Course("AVDM 0170", "DXD", None, 70, 2, 18, 1.5, 1),
                                         Course("AVDM 0138", "DXD", None, 70, 2, 18, 1.5, 1),
                                         Course("DXDI 0103", "DXD", None, 70, 2, 24, 1.5, 1),
                                         Course("DXDI 0104", "DXD", "DXDI 0103", 70, 2, 24, 1.5, 1),
                                         Course("AVDM 0238", "DXD", None, 70, 3, 18, 1.5, 1),
                                         Course("AVDM 0270", "DXD", None, 70, 3, 18, 1.5, 1),
                                         Course("DXDI 9901", "DXD", None, 70, 3, 45, 1.5, 1)],

                                "BK" : [Course("ACCT 0201", "BK", None, 70, 1, 18, 1.5, 0),
                                        Course("ACCT 0202", "BK", None, 70, 1, 12, 1.5, 0),
                                        Course("ACCT 0203", "BK", None, 70, 1, 12, 1.5, 0),
                                        Course("ACCT 0206", "BK", None, 70, 2, 12, 1.5, 0),
                                        Course("ACCT 0210", "BK", None, 70, 2, 28, 1.5, 1),
                                        Course("ACCT 0211", "BK", None, 70, 2, 28, 1.5, 1),
                                        Course("ACCT 0208", "BK", None, 70, 3, 21, 1.5, 1),
                                        Course("ACCT 9901", "BK", None, 70, 3, 33, 1.5, 1)
                                        ]}
        
        self.max_capacity = max_capacity
        self.courses = courses



class Classroom:
    def __init__(self, classroom_id, capacity, class_type):
        self.classroom_id = classroom_id
        self.capacity = capacity
        self.class_type = class_type
        self.time_slot = {"Monday": {"start": 8, "end": 17},\
            "Tuesday": {"start": 8, "end": 17}, \
                "Wednesday": {"start": 8, "end": 17}, \
                    "Thursday": {"start": 8, "end": 17},}

        self.time_slot_lab = {"Monday": {"start": 8, "end": 20},\
            "Tuesday": {"start": 8, "end": 20}, \
                "Wednesday": {"start": 8, "end": 20}, \
                    "Thursday": {"start": 8, "end": 20},}
        self.schedule = {}

    '''
    copy: make identical copy of classrooms so each classroom has a distinct scheduled per term.
    '''
    def copy(self):
        return Classroom(self.classroom_id, self.capacity, self.class_type)
    


class Term:
    def __init__(self, term_id, term_value):
        self.term_id = term_id
        self.term_value = term_value
        self.term_sched = {}
        self.unsched_courses = {}   #unscheduled_courses waiting to be scheduled
        self.track = {} #keep track of all times for each course in prog/core      
        self.term_core_course = []
        self.term_prog_course = []
        self.scheduled_courses = []

    '''
    assign_unsched: if a course cannot be scheduled, it will be appended to a departments(key) unscheduled courses list(values)
    '''
    def assign_unsched(self, course):
        if course.department in self.unsched_courses and course not in self.unsched_courses[course.department]:
            for dep, courses in self.unsched_courses.items():
                if dep == course.department:
                    self.unsched_courses[dep].append(course)
        elif course.department not in self.unsched_courses:
            self.unsched_courses[course.department] = []

    # def display_au(self):
    #     for id, sched in self.unsched_courses.items():
    #         print(id, sched)

    '''
    new_course_time: once we determine the scheduled_course that needs to be replaced, we will find a course that satisfies the time constraints(conditions: no overlap) and swap courses
                     if we cannot find a course that satisfies the time constraints, we will place a None value in its place in case we do find one that does.
        
        parameters: courses; unscheduled courses
            course; course that does not have a pre req
    '''
    def new_course_time(self, classroom, unscheduled_courses, valid_replacemnets, ind):
        for scheduled_course, occurences in ind.items():
            replacement_course = valid_replacemnets[0] # get the first element from valid_replacemnets
            for day, index in occurences.items():
                self.calc_time(classroom, scheduled_course, replacement_course, day, index)
                # use the same replacement course for both subkeys
            for dep, courses in unscheduled_courses.items():
                if valid_replacemnets[0] in courses:
                    courses.remove(valid_replacemnets[0])
            valid_replacemnets.pop(0) # remove the used replacement course from valid_replacemnets
                    



    def calc_time(self, classroom, scheduled_course, valid_replacments, day, ind):
        if scheduled_course.lecture_duration == valid_replacments.lecture_duration:
            valid_replacments.lecture_start_time = scheduled_course.lecture_start_time
            valid_replacments.lecture_end_time = scheduled_course.lecture_end_time
            classroom.schedule[day][ind] = valid_replacments
            
            print(f"{scheduled_course.course_id} is swapped with {valid_replacments.course_id}")
            return
        
        elif scheduled_course.lecture_duration > valid_replacments.lecture_duration: 
            valid_replacments.lecture_start_time = scheduled_course.lecture_start_time
            valid_replacments.lecture_end_time = valid_replacments.lecture_start_time + valid_replacments.lecture_duration
            classroom.schedule[day][ind] = valid_replacments

            print(f"{scheduled_course.course_id} is swapped with {valid_replacments.course_id}")
            return
        
        # if they cannot be swapped, replace old course with None
        else:
            classroom.schedule[day][ind] = None
            print(f"{scheduled_course.course_id} has been removed from schedule")

        

