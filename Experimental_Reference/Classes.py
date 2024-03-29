'''
Author: Victor Tadros
CMPT 395 X03L - Team: 3
Purpose: Build classes for students, degree, program, course, and classroom
'''

class Program:
    def __init__(self, program_id="", core=1, populations=[0,0,0],courselist=[[],[],[]]):
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
    def __init__(self, classroom_id, capacity=0, c_type=0, ghost = 0):
        self.classroom_id = classroom_id
        self.capacity = capacity
        self.c_type = c_type
        self.schedule = {}

    def is_lab(self):
        class_types = ["Lecture", "Lab", "Online", "Virtual"]
        ctype = self.c_type
        return class_types[ctype]

    def __str__(self):
        return f"Classroom({self.classroom_id},{self.capacity},{lab})"
    def __repr__(self):
        lab = self.is_lab()
        return f"Classroom({self.classroom_id},{self.capacity},{lab})"
    
    

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