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
    def __init__(self, course_id, max_capacity, term, transcript_hours, lecture_duration, need_lab_room, online):
        self.course_id = course_id
        self.max_capacity = max_capacity
        self.term = term
        self.transcript_hours = transcript_hours
        self.lecture_duration = lecture_duration
        self.lecture_start_time = 8
        self.lecture_end_time = 9
        self.need_lab_room = need_lab_room
        self.online = online
        # self.sections = []

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
        self.core_courses = {"PCOM": [Course("PCOM 0101", 70, 1, 35, 1.5, False, False),
                        Course("PCOM 0105", 70, 1, 35, 1.5, False, False),
                        Course("PCOM 0107", 70, 1, 18, 3, True, False),
                        Course("PCOM 0233", 70, 1, 7, 1.5, True, False), 
                        Course("PCOM 0235", 70, 1, 6, 1.5, True, False),
                        Course("PCOM 0102", 70, 2, 35, 1.5, False, False),
                        Course("PCOM 0201", 70, 2, 35, 1.5, False, False),
                        Course("PCOM 0108", 70, 2, 18, 1.5, True, False), 
                        Course("PCOM 0202", 70, 3, 33, 1.5, False, False),
                        Course("PCOM 0103", 70, 3, 35, 1.5, False, False),
                        #PCOM 0109 runs in a classroom and lab?
                        ], 
                "BCOM": [Course("PCOM 0203", 70, 1, 15, 1.5, False, False),
                        Course("SUPR 0751", 70, 1, 7, 2, False, False),
                        Course("PCOM 0204", 70, 1, 35, 1.5, False, False),
                        Course("CMSK 0237", 70, 1, 12, 1.5, False, True),
                        Course("SUPR 0837", 70, 1, 7, 2, False, False),
                        Course("SUPR 0841", 70, 1, 35, 2, False, False),
                        Course("SUPR 0821", 70, 2, 7, 2, False, False),
                        Course("SUPR 0822", 70, 2, 7, 2, False, False),
                        Course("SUPR 0718", 70, 2, 7, 2, False, False),
                        Course("SUPR 0836", 70, 2, 7, 2, False, False),
                        Course("AVDM 0199", 70, 2, 3, 1.5, False, True),
                        Course("PCOM 0106", 70, 2, 35, 2, False, False), #schedule for 17 sessions
                        Course("PCOM 0205", 70, 3, 30, 3, False, False),
                        Course("PCOM TBD", 70, 3, 21, 1.5, False, False),
                        Course("PCOM 0207", 70, 3, 6, 2, False, False),
                        Course("SUPR 0863", 70, 3, 7, 2, False, False),
                        Course("PCOM 0206", 70, 3, 6, 3, False, False),
                        Course("AVDM 0260", 70, 3, 6, 1.5, False, True) #schedule after all calsses are done, end of the term
                        ]}


class Program:
    def __init__(self, max_capacity, courses):
        self.program_id = ["PM", "BA", "GLM", "FS", "DXD", "BK"]
        self.max_capacity = max_capacity
        self.courses = courses


class Classroom:
    def __init__(self, classroom_id, capacity, lab_room):
        self.classroom_id = classroom_id
        self.capacity = capacity
        self.lab_room = lab_room
        self.time_slot = {"Monday": {"start": 8, "end": 17},\
            "Tuesday": {"start": 8, "end": 17}, \
                "Wednesday": {"start": 8, "end": 17}, \
                    "Thursday": {"start": 8, "end": 17},}

        self.time_slot_lab = {"Monday": {"start": 8, "end": 20},\
            "Tuesday": {"start": 8, "end": 20}, \
                "Wednesday": {"start": 8, "end": 20}, \
                    "Thursday": {"start": 8, "end": 20},}
        self.schedule = {}
