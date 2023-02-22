'''
Author: Victor Tadros
CMPT 395 X03L - Team: 3
Purpose: Test methods from courseClass
'''

import unittest
from courseClass import *

class TestStudentSchedule(unittest.TestCase):

    def test_schedule_core_courses(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        degree = Degree()
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", 36, 1, 15, 1.5, False, False), 
                    Course("SUPR 0751", 36, 1, 7, 1.5, False, False), 
                    Course("PRDV 0201", 20, 1, 21, 1.5, False, False),
                    Course("PRDV 0202", 20, 1, 14, 1.5, False, False),
                    Course("FODDER 101", 40, 1, 40, 3, False, False)]
        classrooms = [Classroom("11-533", 36, False), 
                        Classroom("11-534", 36, False),
                        Classroom("11-560", 24, False), 
                        Classroom("11-533", 24, False)]
        schedule = Schedule(student, degree, program, courses, classrooms)

        print(f"\n==================\n=================")
        print(f"\n=====Testing schedule_core_courses=====\n")
        print(f"==================\n=================")

        schedule.schedule_course(courses[1], "Monday", classrooms[0])
        schedule.schedule_course(courses[2], "Monday", classrooms[0])
        schedule.schedule_course(courses[4], "Monday", classrooms[0])
        schedule.schedule_course(courses[3], "Monday", classrooms[0])
        schedule.schedule_course(courses[0], "Monday", classrooms[0])

        schedule.schedule_core_courses()
        for classroom in classrooms:
            schedule.display_schedule(classroom)     


    def test_check_availability(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        degree = Degree()
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", 36, 1, 15, 1.5, False, False), 
                    Course("SUPR 0751", 36, 1, 7, 1.5, False, False), 
                    Course("PRDV 0201", 20, 1, 21, 1.5, False, False),
                    Course("PRDV 0202", 20, 1, 14, 1.5, False, False),
                    Course("FODDER 101", 40, 1, 40, 3, False, False)]
        classrooms = [Classroom("11-533", 36, False), 
                        Classroom("11-534", 36, False),
                        Classroom("11-560", 24, False), 
                        Classroom("11-533", 24, False)]
        schedule = Schedule(student, degree, program, courses, classrooms)

        # Test when there is no course scheduled on the given day
        self.assertTrue(schedule.check_availability(courses[0], "Monday", classrooms[0]))

        schedule.schedule_course(courses[1], "Monday", classrooms[0])
        schedule.schedule_course(courses[2], "Monday", classrooms[0])
        schedule.schedule_course(courses[4], "Monday", classrooms[0])
        schedule.schedule_course(courses[3], "Monday", classrooms[0])
        schedule.schedule_course(courses[0], "Monday", classrooms[0])

        # Test when course cannot fit in time slot
        self.assertFalse(schedule.check_availability(courses[1], "Monday", classrooms[0]))

    def test_course_occurences(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        degree = Degree()
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", 36, 1, 15, 1.5, False, False), 
                    Course("SUPR 0751", 36, 1, 7, 1.5, False, False), 
                    Course("PRDV 0201", 20, 1, 21, 1.5, False, False),
                    Course("PRDV 0202", 20, 1, 14, 1.5, False, False),
                    Course("FODDER 101", 40, 1, 40, 3, False, False)]
        classrooms = [Classroom("11-533", 36, False), 
                        Classroom("11-534", 36, False),
                        Classroom("11-560", 24, False), 
                        Classroom("11-533", 24, False)]
        schedule = Schedule(student, degree, program, courses, classrooms)

        print(f"\n==================\n=================")
        print(f"\n=====Testing course_occurence=====")
        print(f"==================\n=================")

        schedule.schedule_course(courses[1], "Monday", classrooms[1])
        self.assertTrue(schedule.course_occurence(courses[1], "Monday", classrooms[1]))
        schedule.schedule_course(courses[2], "Monday", classrooms[1])
        self.assertTrue(schedule.course_occurence(courses[1], "Monday", classrooms[1]))
        schedule.schedule_course(courses[1], "Monday", classrooms[1])
        self.assertFalse(schedule.course_occurence(courses[1], "Monday", classrooms[1]))


        schedule.display_schedule(classrooms[1])
        print("\n")



    def test_schedule_course(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        degree = Degree()
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", 36, 1, 15, 1.5, False, False), 
                    Course("SUPR 0751", 36, 1, 7, 1.5, False, False), 
                    Course("PRDV 0201", 20, 1, 21, 1.5, False, False),
                    Course("PRDV 0202", 20, 1, 14, 1.5, False, False),
                    Course("FODDER 101", 40, 1, 40, 3, False, False)]
        classrooms = [Classroom("11-533", 36, False), 
                        Classroom("11-534", 36, False),
                        Classroom("11-560", 24, False), 
                        Classroom("11-533", 24, False)]
        schedule = Schedule(student, degree, program, courses, classrooms)

        print(f"\n==================\n=================")
        print(f"\n=====Testing schedule_course=====\n")
        print(f"==================\n=================")

        schedule.schedule_course(courses[1], "Monday", classrooms[1])
        schedule.schedule_course(courses[2], "Monday", classrooms[1])
        schedule.schedule_course(courses[4], "Monday", classrooms[1])
        schedule.schedule_course(courses[3], "Monday", classrooms[1])

        schedule.display_schedule(classrooms[1])
        print("\n")


    def test_replace_course(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        degree = Degree()
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", 36, 1, 15, 1.5, False, False), 
                    Course("SUPR 0751", 36, 1, 7, 1.5, False, False), 
                    Course("PRDV 0201", 20, 1, 21, 1.5, False, False),
                    Course("PRDV 0202", 20, 1, 14, 1.5, False, False),
                    Course("FODDER 101", 40, 1, 0, 3, False, False)]
        classrooms = [Classroom("11-533", 36, False), 
                        Classroom("11-534", 36, False),
                        Classroom("11-560", 24, False), 
                        Classroom("11-533", 24, False)]
        schedule = Schedule(student, degree, program, courses, classrooms)

        print(f"==================\n=================")
        print(f"\n=====Testing replace_course=====\n")
        print(f"==================\n=================")
        schedule.schedule_course(courses[1], "Monday", classrooms[1])
        schedule.schedule_course(courses[2], "Monday", classrooms[1])
        schedule.schedule_course(courses[4], "Monday", classrooms[1])
        schedule.schedule_course(courses[3], "Monday", classrooms[1])

        schedule.replace_course(courses[0], "Monday", classrooms[1])

        schedule.display_schedule(classrooms[1])
        print("\n")


    def test_fill_empty_spot(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        degree = Degree()
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", 36, 1, 15, 2, False, False), 
                    Course("SUPR 0751", 36, 1, 0, 1.5, False, False), 
                    Course("PRDV 0201", 20, 1, 21, 1.5, False, False),
                    Course("PRDV 0202", 20, 1, 14, 1.5, False, False),
                    Course("FODDER 101", 40, 1, 10, 3, False, False),
                    Course("STUFF 202", 20, 1, 15, 1.5, False, False)]
        classrooms = [Classroom("11-533", 36, False), 
                        Classroom("11-534", 36, False),
                        Classroom("11-560", 24, False), 
                        Classroom("11-533", 24, False)]
        schedule = Schedule(student, degree, program, courses, classrooms)

        print(f"\n================\n===================")
        print(f"\n=====Testing fill_empty_spot=====\n")
        print(f"==================\n=================")

        schedule.schedule_course(courses[1], "Monday", classrooms[1])
        schedule.schedule_course(courses[2], "Monday", classrooms[1])
        schedule.schedule_course(courses[4], "Monday", classrooms[1])
        schedule.schedule_course(courses[3], "Monday", classrooms[1])

        
        schedule.replace_course(courses[0], "Monday", classrooms[1])
        
        schedule.display_schedule(classrooms[1])
        print("\n")
        
        schedule.fill_empty_spot(courses[5], "Monday", classrooms[1])

        schedule.display_schedule(classrooms[1])
        print("\n")


if __name__ == '__main__':
    unittest.main()