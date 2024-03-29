'''
Author: Victor Tadros
CMPT 395 X03L - Team: 3
Purpose: Build classes for students, degree, program, course, and classroom
'''

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
    def __init__(self, program_id="", core=1, populations=[0,0,0],courselist=[[],[],[]] ):
        self.program_id = program_id
        self.core = core
        self.populations = populations
        self.courselist = courselist

        self.courses = []
        

        
    def __repr__(self):
        string = self.program_id
        return str("[" + string + ": " + ", ".join(str(i) for i in self.courses) + "]")

class Course:
    def __init__(self, course_id="None", name="", class_type=1, preq=None, transcript_hours=0, lecture_duration=0, 
                 lecture_start_time = 8, lecture_end_time = 17, cap = 0, department = ""):

        self.course_id = course_id
        self.name = name

        # changing this to class_type
        # 1 = Lecture
        # 2 = Lab
        # 3 = Online
        # 4 = Virtual (No Scheduling)
        self.class_type = class_type
        self.department = department
        self.preq = preq
        self.transcript_hours = transcript_hours
        self.lecture_duration = lecture_duration
        self.lecture_start_time = lecture_start_time
        self.lecture_end_time = lecture_end_time
        self.cap = cap

        # This is the item I will use for prereq checks. This finds the last day this
        # class was scheduled
        self.last_day = None

    def __repr__(self):
        return str(self.course_id + ": " + self.name)

# ---------------------------------------------------
# -- Classroom class we will populate into a list later.
# ---------------------------------------------------
class Classroom:
    def __init__(self, classroom_id, c_type=0, capacity=0):
        self.classroom_id = classroom_id
        self.capacity = capacity
        self.c_type = c_type
        self.schedule = {}

    def is_lab(self):
        class_types = ["Lecture", "Lab", "Online", "Virtual"]
        ctype = self.c_type
        return class_types[ctype]

    def __repr__(self):
        lab = self.is_lab()
        return str("\n"+self.classroom_id + " - " + lab + " - " + str(self.capacity))
    
    

def add_course( program,course_id="None", name="", term = 1, class_type=1, preq=None, transcript_hours=0, lecture_duration=0, 
                lecture_start_time = 8, lecture_end_time = 17, cap = 0, department = ""):
        
        courses = program.courses
        for item in courses:
            if item == course_id:
                print("Class Conflict. Overwrite? (exiting for now)")
                return None

        course = Course(course_id, name, class_type, preq, transcript_hours, lecture_duration,
                        lecture_start_time, lecture_end_time, cap, department)
        
        program.courses.append(course_id)
        program.courselist[term-1].append(course)