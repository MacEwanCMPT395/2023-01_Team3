import unittest
from courseClass import *

class TestStudentSchedule(unittest.TestCase):
    def test_check_availability(self):
        student = Student(1, "John Doe", "BCOM", "PM", "Term 1")
        degree = Degree("BCOM", ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        program = Program("BCOM", 150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", 36, "Term 1", 15, 1.5), 
                    Course("SUPR 0751", 36, "Term 1", 7, 1.5), 
                    Course("PRDV 0201", 20, "Term 1", 21, 1.5),
                    Course("PRDV 0202", 20, "Term 1", 14, 1.5)]
        classrooms = [Classroom("11-533", 36, False), 
                        Classroom("11-534", 36, False),
                        Classroom("11-560", 24, False), 
                        Classroom("11-533", 24, False)]
        schedule = Schedule(student, degree, program, courses, classrooms)
        
        # Test when there is no course scheduled on the given day
        self.assertTrue(schedule.check_availability(courses[0], "Monday", classrooms[0]))

        # Test when the course is scheduled in a different classroom
        classrooms[1].schedule["Monday"] = [(courses[0])]
        self.assertTrue(schedule.check_availability(courses[1], "Monday", classrooms[0]))

        # Failing test
        # classrooms[1].schedule["Monday"] = [(courses[1])]
        # self.assertFalse(schedule.check_availability(courses[2], "Monday", classrooms[1]))

    def test_course_occurences(self):
        student = Student(1, "John Doe", "BCOM", "PM", "Term 1")
        degree = Degree("BCOM", ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        program = Program("BCOM", 150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", 36, "Term 1", 15, 1.5), 
                    Course("SUPR 0751", 36, "Term 1", 7, 1.5), 
                    Course("PRDV 0201", 20, "Term 1", 21, 1.5),
                    Course("PRDV 0202", 20, "Term 1", 14, 1.5),
                    Course("FODDER 101", 40, "Term 1", 40, 3)]
        classrooms = [Classroom("11-533", 36, False), 
                        Classroom("11-534", 36, False),
                        Classroom("11-560", 24, False), 
                        Classroom("11-533", 24, False)]
        schedule = Schedule(student, degree, program, courses, classrooms)

        schedule.schedule_course(courses[1], "Monday", classrooms[1])
        self.assertTrue(schedule.course_occurence(courses[1], "Monday", classrooms[1]))
        schedule.schedule_course(courses[2], "Monday", classrooms[1])
        self.assertTrue(schedule.course_occurence(courses[1], "Monday", classrooms[1]))
        schedule.schedule_course(courses[1], "Monday", classrooms[1])
        self.assertFalse(schedule.course_occurence(courses[1], "Monday", classrooms[1]))


        schedule.display_schedule(classrooms[1])
        print("\n")



    def test_schedule_course(self):
        student = Student(1, "John Doe", "BCOM", "PM", "Term 1")
        degree = Degree("BCOM", ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        program = Program("BCOM", 150, ["PCOM 0203", "SUPR 0751", "PCOM0204", "CMSK 0237", "SUPR 0837", "SUPR 0841"])
        courses = [Course("PCOM 0203", 36, "Term 1", 15, 1.5), 
                    Course("SUPR 0751", 36, "Term 1", 7, 1.5), 
                    Course("PRDV 0201", 20, "Term 1", 21, 1.5),
                    Course("PRDV 0202", 20, "Term 1", 14, 1.5),
                    Course("FODDER 101", 40, "Term 1", 40, 3)]
        classrooms = [Classroom("11-533", 36, False), 
                        Classroom("11-534", 36, False),
                        Classroom("11-560", 24, False), 
                        Classroom("11-533", 24, False)]
        schedule = Schedule(student, degree, program, courses, classrooms)

        schedule.schedule_course(courses[1], "Monday", classrooms[1])
        schedule.schedule_course(courses[2], "Monday", classrooms[1])
        schedule.schedule_course(courses[4], "Monday", classrooms[1])
        schedule.schedule_course(courses[3], "Monday", classrooms[1])

        schedule.display_schedule(classrooms[1])


if __name__ == '__main__':
    unittest.main()