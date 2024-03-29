'''
Author: Victor Tadros
CMPT 395 X03L - Team: 3
Purpose: Test methods from courseClass
'''

import unittest
from new_scheduler import *

class TestStudentSchedule(unittest.TestCase):


    def test_display_classroom(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        # degree = Degree()
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", "PCOM", None, 36, 1, 15, 1.5, 0), 
                    Course("SUPR 0751", "PCOM", None, 36, 1, 7, 1.5, 0), 
                    Course("PRDV 0201", "PCOM", None, 20, 1, 21, 1.5, 0),
                    Course("PRDV 0202", "PCOM", None, 20, 1, 14, 1.5, 0),
                    Course("FODDER 101", "PCOM", None, 40, 1, 40, 3, 0)]
        classrooms = [Classroom("11-532", 30, 1),
                        Classroom("Online", 40, 2), 
                        Classroom("11-533", 36, 0),
                        Classroom("11-534", 36, 0),
                        Classroom("11-560", 24, 0), 
                        Classroom("11-562", 24, 0),
                        Classroom("11-564", 24, 0),
                        Classroom("11-458", 40, 0),
                        Classroom("11-430", 30, 0),
                        Classroom("11-320", 30, 0)]
        term = [Term("Term 1", 1), 
                Term("Term 2", 2),
                Term("Term 3", 3)]
        schedule = Schedule(student, program, courses, classrooms, term)

        # print(f"\n===================================")
        # print(f"\n=====Testing display_classroom=====\n")

        # schedule.term_schedule(classrooms, term)
        # schedule.display_classroom(term[1], classrooms[0])

        # print(f"===================================")


    def test_term_schedule(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", "PCOM", None, 36, 1, 15, 1.5, 0), 
                    Course("SUPR 0751", "PCOM", None, 36, 1, 7, 1.5, 0), 
                    Course("PRDV 0201", "PCOM", None, 20, 1, 21, 1.5, 0),
                    Course("PRDV 0202", "PCOM", None, 20, 1, 14, 1.5, 0),
                    Course("FODDER 101", "PCOM", None, 40, 1, 40, 3, 0)]
        classrooms = [Classroom("11-532", 30, 1),
                      Classroom("Online", 40, 2),
                        Classroom("11-533", 36, 0), 
                        Classroom("11-534", 36, 0),
                        Classroom("11-560", 24, 0), 
                        Classroom("11-562", 24, 0),
                        Classroom("11-564", 24, 0),
                        Classroom("11-458", 40, 0),
                        Classroom("11-430", 30, 0),
                        Classroom("11-320", 30, 0)]
        term = [Term("Term 1", 1), 
                Term("Term 2", 2),
                Term("Term 3", 3)]
        schedule = Schedule(student, program, courses, classrooms, term)

        print(f"\n===================================")
        print(f"\n=====Testing term_schedule=====\n")

        schedule.term_schedule(classrooms, term)
        schedule.display_term(term)

        # for t in term:
        #         print(t.term_id, t.track)

        #To view unsched courses for each term
        # for t in term:
        #         print(t.term_id)
        #         for dep, crs in t.unsched_courses.items():
        #                 print(f"\t{dep}")
        #                 for c in crs:
        #                      print(f"\t\t{c.course_id}")

        print(f"===================================")
        

    def test_check_availability(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", "PCOM", None, 36, 1, 15, 1.5, 0), 
                    Course("SUPR 0751", "PCOM", None, 36, 1, 7, 1.5, 0), 
                    Course("PRDV 0201", "PCOM", None, 20, 1, 21, 1.5, 0),
                    Course("PRDV 0202", "PCOM", None, 20, 1, 14, 1.5, 0),
                    Course("FODDER 101", "PCOM", None, 40, 1, 40, 3, 0)]
        classrooms = [Classroom("11-533", 36, 0), 
                        Classroom("11-534", 36, 0),
                        Classroom("11-560", 24, 0), 
                        Classroom("11-562", 24, 0),
                        Classroom("11-564", 24, 0),
                        Classroom("11-458", 40, 0),
                        Classroom("11-430", 30, 0),
                        Classroom("11-320", 30, 0),
                        Classroom("11-532", 30, 1)]
        term = [Term("Term 1", 1), 
                Term("Term 2", 2),
                Term("Term 3", 3)]
        schedule = Schedule(student, program, courses, classrooms, term)

        print(f"\n===================================")
        print(f"\n=====Testing check_availability=====\n")

        # Test when there is no course scheduled on the given day
        self.assertTrue(schedule.check_availability(courses[0], "Monday", classrooms[0]))

        schedule.schedule_course(courses[1], "Monday", classrooms[0], term[0]) #9.5
        schedule.schedule_course(courses[2], "Monday", classrooms[0], term[0]) #11
        schedule.schedule_course(courses[4], "Monday", classrooms[0], term[0]) #14
        schedule.schedule_course(courses[3], "Monday", classrooms[0], term[0]) #15.5
        schedule.schedule_course(courses[0], "Monday", classrooms[0], term[0]) #17

        # Test when course cannot fit in time slot
        self.assertFalse(schedule.check_availability(courses[1], "Monday", classrooms[0]))
        print(f"===================================")


    def test_schedule_course(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", "PCOM", None, 36, 1, 15, 1.5, 0), 
                    Course("SUPR 0751", "PCOM", None, 36, 1, 7, 1.5, 0), 
                    Course("PRDV 0201", "PCOM", None, 20, 1, 21, 1.5, 0),
                    Course("PRDV 0202", "PCOM", None, 20, 1, 14, 1.5, 0),
                    Course("FODDER 101", "PCOM", None, 40, 1, 40, 3, 0)]
        classrooms = [Classroom("11-533", 36, 0), 
                        Classroom("11-534", 36, 0),
                        Classroom("11-560", 24, 0), 
                        Classroom("11-562", 24, 0),
                        Classroom("11-564", 24, 0),
                        Classroom("11-458", 40, 0),
                        Classroom("11-430", 30, 0),
                        Classroom("11-320", 30, 0),
                        Classroom("11-532", 30, 1)]
        term = [Term("Term 1", 1), 
                Term("Term 2", 2),
                Term("Term 3", 3)]
        schedule = Schedule(student, program, courses, classrooms, term)

        # print(f"\n===================================")
        # print(f"\n=====Testing schedule_course=====\n")

        # schedule.schedule_course(courses[1], "Monday", classrooms[1])
        # schedule.schedule_course(courses[2], "Monday", classrooms[1])
        # schedule.schedule_course(courses[4], "Monday", classrooms[1])
        # schedule.schedule_course(courses[3], "Monday", classrooms[1])

        # schedule.display_schedule(classrooms[1])
        # print("\n")
        # print(f"===================================")


    def test_replace_course(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", "PCOM", None, 36, 1, 15, 1.5, 0), 
                    Course("SUPR 0751", "PCOM", None, 36, 1, 7, 1.5, 0), 
                    Course("PRDV 0201", "PCOM", None, 20, 1, 21, 1.5, 0),
                    Course("PRDV 0202", "PCOM", None, 20, 1, 14, 1.5, 0),
                    Course("FODDER 101", "PCOM", None, 40, 1, 40, 3, 0)]
        classrooms = [Classroom("11-532", 30, 1),
                        Classroom("Online", 40, 2), 
                        Classroom("11-533", 36, 0),
                        Classroom("11-534", 36, 0),
                        Classroom("11-560", 24, 0), 
                        Classroom("11-562", 24, 0),
                        Classroom("11-564", 24, 0),
                        Classroom("11-458", 40, 0),
                        Classroom("11-430", 30, 0),
                        Classroom("11-320", 30, 0)]
        term = [Term("Term 1", 1), 
                Term("Term 2", 2),
                Term("Term 3", 3)]
        schedule = Schedule(student, program, courses, classrooms, term)

        # print(f"\n===================================")
        # print(f"\n=====Testing replace_course=====\n")

        # schedule.term_schedule(classrooms, term)
        # schedule.display_classroom(term[1], classrooms[0])

        # for trm, val in term[1].term_sched.items():
        #     for classrooms in val:
        #         schedule.replace_course(term[1], classrooms)
                
        # schedule.display_classroom(term[1], classrooms[0])

        # print(f"===================================")


    def test_fill_empty_spot(self):
        student = Student(1, "John Doe", "BCOM", "PM", 1)
        program = Program(150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", "PCOM", None, 36, 1, 15, 1.5, 0), 
                    Course("SUPR 0751", "PCOM", None, 36, 1, 7, 1.5, 0), 
                    Course("PRDV 0201", "PCOM", None, 20, 1, 21, 1.5, 0),
                    Course("PRDV 0202", "PCOM", None, 20, 1, 14, 1.5, 0),
                    Course("FODDER 101", "PCOM", None, 40, 1, 40, 3, 0),
                    Course("STUFF 202", "PCOM", None, 40, 1, 0, 1.5, 0)]
        classrooms = [Classroom("11-533", 36, 0), 
                        Classroom("11-534", 36, 0),
                        Classroom("11-560", 24, 0), 
                        Classroom("11-562", 24, 0),
                        Classroom("11-564", 24, 0),
                        Classroom("11-458", 40, 0),
                        Classroom("11-430", 30, 0),
                        Classroom("11-320", 30, 0),
                        Classroom("11-532", 30, 1)]
        terms = [Term("Term 1", 1), 
                Term("Term 2", 2),
                Term("Term 3", 3)]
        schedule = Schedule(student, program, courses, classrooms, terms)
        terms[0].unsched_courses = {"PCOM" : [Course("PCOM !!!!", "PCOM", None, 36, 1, 15, 1.5, 0), 
                                            Course("SUPR ****", "PCOM", None, 36, 1, 7, 1.5, 0), 
                                            Course("PRDV @@@@", "PCOM", None, 20, 1, 21, 1.5, 0)],
                            
                                    "BCOM" : [Course("PRDV ####", "PCOM", None, 20, 1, 14, 1.5, 0),
                                            Course("FODDER $$$$", "PCOM", None, 40, 1, 40, 3, 0)]}

        # print(f"\n===================================")
        # print(f"\n=====Testing fill_empty_spot=====\n")

        # schedule.schedule_course(courses[1], "Monday", classrooms[1])
        # schedule.schedule_course(courses[2], "Monday", classrooms[1])
        # schedule.schedule_course(courses[5], "Monday", classrooms[1])
        # schedule.schedule_course(courses[3], "Monday", classrooms[1])

        
        # schedule.replace_course(terms[0], classrooms)
        
        # schedule.display_schedule(classrooms[1])
        # print("\n")
        
        # schedule.fill_empty_spot(terms[0], classrooms)

        # schedule.display_schedule(classrooms[1])
        # print("\n")
        # print(f"===================================")

    def test_read_csv(self):
        print(f"\n===================================")
        print(f"\n=====Testing read_csv=====\n")
        # Please note I need to figure out how to change path so it's more universal but for now I use my own path on my PC
        # For this test to work please put in the path to the csv to read
        courses, program = read_csv("C:\\Users\\SJsni\\Documents\\project395\\2023-01_Team3\\Experimental_Reference\\CSV Files\\classes.csv")
        for i in range(len(courses)):
                print(courses[i].course_id)
        print("\n")
        print(f"===================================")


if __name__ == '__main__':
    unittest.main()
