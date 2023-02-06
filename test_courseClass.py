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
        self.assertTrue(schedule.check_availability("Monday", classrooms[0], lecture_start_time=8))

        # Test when the course is scheduled in a different classroom
        schedule.schedule["Monday"] = [(courses[0], classrooms[1])]
        self.assertTrue(schedule.check_availability("Monday", classrooms[0], lecture_start_time=8))

        # Test when the course is scheduled in the same classroom
        self.assertFalse(schedule.check_availability("Monday", classrooms[1], lecture_start_time=8))

        # Test when there is overlap in time
        schedule.schedule["Monday"].append((courses[1], classrooms[1]))
        self.assertFalse(schedule.check_availability("Monday", classrooms[1], lecture_start_time=9))
        
    def test_check_time_slot(self):
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
        
        # Test when the start time is within the time slot
        
        self.assertTrue(schedule.check_time_slot("Monday", classrooms[0], lecture_start_time=9))
        
        # Test when the end time is outside the time slot
        
        self.assertFalse(schedule.check_time_slot("Monday", classrooms[0]), lecture_start_time=16)

if __name__ == '__main__':
    unittest.main()