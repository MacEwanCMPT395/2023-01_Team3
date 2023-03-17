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
        self.class_type = class_type
        self.department = department
        self.preq = preq
        self.transcript_hours = transcript_hours
        self.lecture_duration = lecture_duration
        self.lecture_start_time = lecture_start_time
        self.lecture_end_time = lecture_end_time
        self.cap = cap

    def __repr__(self):
        return str(self.course_id + ": " + self.name)

# ---------------------------------------------------
# -- Classroom class we will populate into a list later.
# ---------------------------------------------------
class Classroom:
    def __init__(self, classroom_id, capacity=0, lab_room=0):
        self.classroom_id = classroom_id
        self.capacity = capacity
        self.lab_room = lab_room
        self.schedule = {}

    def __repr__(self):
        lab = (self.lab_room) and "Lab" or "Lecture"
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