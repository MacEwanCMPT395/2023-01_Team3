class Student:
    def __init__(self, student_id, name, degree, program, term):
        self.student_id = student_id
        self.name = name
        self.degree = degree
        self.program = program
        self.term = term


class Course:
    def __init__(self, course_id="None", name="", course_type=1, preq=None, transcript_hours=0, lecture_duration=0, 
                 term = None, lecture_start_time = 8, lecture_end_time = 17, cap = 0, department = ""):
        self.course_id = course_id
        self.name = name
        self.department = department
        self.pre_req = preq
        self.cap = cap
        self.term = term
        self.transcript_hours = transcript_hours
        self.lecture_duration = lecture_duration
        self.lecture_start_time = lecture_start_time
        self.lecture_end_time = lecture_end_time
        self.course_type = course_type
        # self.count = 0
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

    '''
    copy: make identical copy of courses so each course has a distinct start and end time.
    '''
    def copy(self, courses):
        copy_courses = []
        for id, crs in courses.items():
            for course in crs:
                copy_courses.append(Course(course.course_id, course.department, course.pre_req, course.max_capacity, course.term, course.transcript_hours, course.lecture_duration, course.course_type))
        return copy_courses
    
    def __repr__(self):
        return str(self.course_id + ": " + self.name)




class Program:
    def __init__(self, program_id = "", courses = [], core = 1, populations = [0,0,0]):
        self.courses = courses
        self.program_id = program_id
        self.core = core
        self.populations = populations #population of program for each term

    def copy(self):
        return Program(self.program_id, self.courses, self.core, self.populations)

    def __repr__(self):
        string = self.program_id
        return str("[" + string + ": " + ", ".join(str(i) for i in self.courses) + "]")



class Classroom:
    def __init__(self, classroom_id, capacity = 0, class_type = 0):
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
    
    
    def __repr__(self):
        lab = (self.lab_room) and "Lab" or "Lecture"
        return str("\n"+self.classroom_id + " - " + lab + " - " + str(self.capacity))

    


class Term:
    def __init__(self, term_id, term_value):
        self.term_id = term_id
        self.term_value = term_value
        self.term_sched = {}
        self.unsched_courses = {}   #unscheduled_courses waiting to be scheduled
        self.track = {} #keep track of all times for each course in prog/core      
        self.term_courses = []
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
