# days is a list of teachable days.
from Time_Stuff import days

import Classes as classes
from open_csv import programs, classrooms
import closest_sum

'''
print()
print(programs,"\n")
print(classrooms,"\n")

for i,j in days.items():
    print(i,j,"\n")

print(days["Monday"])
'''


'''
Program Info:

def __init__(self, program_id="", core=1, populations=[0,0,0],courselist=[[],[],[]]):

Course Info:

def __init__(self, course_id="None", name="", class_type=1, preq=None, transcript_hours=0, lecture_duration=0, 
             lecture_start_time = 8, lecture_end_time = 17, grace = 1):

Classroom info:

def __init__(self, classroom_id, capacity, lab_room=0):

Days Info:

# Monday through friday.
Day: {
        "Monday": { List of days }
        "Tuesday": { List of days }
}
'''

class Schedule:
    def __init__(self, programs, classrooms,space = 2):
        self.programs = programs
        self.classrooms = classrooms
        self._space = 2 # space for the classroom capacity

        # insert online classroom
        
        self.classrooms.append(classes.Classroom("Virtual",-1,2))

        self._schedule = {"Monday":[],
                         "Tuesday":[],
                         "Wednesday":[],
                         "Thursday":[],
                         "Virtual":[]}

        # for now no need for friday and saturday, but can easily be added.
        self.schedule = {classroom:dict(days) for classroom in classrooms}
        print(self.schedule)

        #print(self.classrooms)

    def check_availability(self,course,days):
        for weekday in days:
            temp = self.schedule[weekday]
            for day in temp:
                for classrooms in day:
                    print()

    def insert_class(self,id,time,classroom,days):
        print()

    def earliest_time_for_class(self):
        print()

    def combine_dates(self, days):

        # This would work for mon, wed, fri classes.
        dict_combined = {}

        for classroom in (self.classrooms):
            dict_combined[classroom] = {}
            for dow in days: #dow = day of week
                for dates, times in self.schedule[classroom][dow].items():
                    if dates in dict_combined[classroom]:
                        dict_combined[classroom][dates].append(times)
                    else:
                        dict_combined[classroom][dates] = times

            # Sort our dictionary.
            keys_sort = list(dict_combined[classroom].keys())
            keys_sort.sort()

            sorted_dict = {i: dict_combined[classroom][i] for i in keys_sort}

            dict_combined[classroom] = sorted_dict

        return dict_combined

    '''
    def __init__(self, course_id="None", name="", class_type=1, preq=None, transcript_hours=0, lecture_duration=0, 
             lecture_start_time = 8, lecture_end_time = 17, cap = 1):
    '''

    def find_range_differences(self, min_max, data_ranges):
        '''
        Use this function to find the times that are FREE.
        To use this function, you can call it like this:
        range_to_compare = [8, 17]
        data_ranges = [[8.5, 9], [9, 11], [13, 15]]
        differences = find_range_differences(range_to_compare, data_ranges)
        print(differences)

        Output: [(8, 8.5), (11, 13), (15, 17)]
        '''
        differences = []
        for data_range in data_ranges:
            if (not data_range): continue
            # Check if the data range overlaps with the range to compare against
            if data_range[1] > min_max[0] and data_range[0] < min_max[1]:
                # Find the non-overlapping parts of the range and add them to the differences list
                if data_range[0] < min_max[0]:
                    differences.append((data_range[0], min_max[0]))
                if data_range[1] > min_max[1]:
                    differences.append((min_max[1], data_range[1]))
            else:
                # If there is no overlap, add the entire data range to the differences list
                differences.append((data_range[0], data_range[1]))
        return differences or [min_max]
    
    def find_range_overlaps(self, range_set1, range_set2):
        '''
        We use this to find overlapping times. We will call this repeatedly
        to find times throughout a semseter that are free, by calling the result
        on the next set of ranges.

        You can call it like this:
        range_set1 = [(8, 8.5), (11, 13), (15, 17)]
        range_set2 = [(8, 9), (10, 12), (13, 16)]
        overlaps = find_range_overlaps(range_set1, range_set2)
        print(overlaps)

        Output: [(8, 8.5), (11, 12), (15, 16)]
        '''

        overlaps = []
        for range1 in range_set1:
            for range2 in range_set2:
                # Check if there is an overlap between the two ranges
                if range1[1] > range2[0] and range1[0] < range2[1]:
                    # Find the overlapping part and add it to the overlaps list
                    overlap_start = max(range1[0], range2[0])
                    overlap_end = min(range1[1], range2[1])
                    overlaps.append((overlap_start, overlap_end))

        return overlaps

    def calculate_space(self,population,courses,classroom_dates):
        factor = len(courses)
        dateset = False

        # Scheduling within a cohort:
        # Once one class is scheduled, the next 2 cannot
        # be scheduled at the same time
        illegal_times = []
        times_to_schedule = []

        # Find possible times one course at a time.
        # We then divide these possible times into our cohort.
        for course in courses:
            duration = course.lecture_duration

            time_restraint = [course.lecture_start_time, course.lecture_end_time]

            # Course cap will determine if we schedule backwards.
            # Schedule backwards = schedule from halfway through the term or
            # the absolute minimum start time (if there's too many hours, say,
            # 20 hours, we will have to start earlier than halfway)
            # Think: (min(half, abs minimum start time))
            # We can calculate and compare the dates.
            cap = course.cap

            # This block of code is confusing because atm lab_room is actually
            # classroom type. So we compare the class type to the classroom type.
            # Then, we assign the class type of the course to the class type
            # of the classroom and populate the real_dates with the class type

            # essentially, real_dates is taken from our REAL schedule and
            # disregards the irrelevant classrooms.

            # real_dates is taken from our real schedule. We do not write to real_dates. It is data
            # to be read!!!
            real_dates = {}
            for i in range(3):
                if (course.class_type == i+1):

                    for classroom,dates in classroom_dates.items():

                        if classroom.lab_room == i:

                            real_dates[classroom] = dates

                    break
            
            # grace = the number of extra classes to be scheduled. If we have room, add one.
            grace = 1

            # int divide
            total_classes = (course.transcript_hours) // duration
            total_classes = int((total_classes+grace <= len(dates)) and total_classes + grace or total_classes)
            #print(course.transcript_hours,duration)
            
            # times to schedule is possible times to schedule for ONE and only ONE course type.
            times_to_schedule = []

            # dummy variable so far
            able_to_schedule = 0

            # recall that real_dates is structured as follows:
            # {
            # Classroom ID[1]: {    date[1]:    [ [(start, end),course ID], [(start, end),course ID] ],
            #                       date[n]:    [ [(start, end),course ID], [(start, end),course ID] ]
            #               },
            # Classroom ID[n]: {    date[1]:    [ [(start, end),course ID], [(start, end),course ID] ],
            #                       date[n]:    [ [(start, end),course ID], [(start, end),course ID] ]
            #               }
            # }

            # So, our loop does the following:
            # loop through the classrooms and dates
            # for each date and times pair, copy the times of each class that's running
            # since we don't care about the class ID's, just the times that are blocked.

            # Finally, find the FREE blocks of time using find_range_differences on the
            # blocked times to create a list of free times we can schedule for a given day.
            print("FUCK: ", real_dates)
            for classroom,dates in real_dates.items():
                free_time = []
                for day, times in dates.items():
                    # Should create a list of lists or something of that nature. [[time range], class/cohort]
                    # doing element[0] should copy just the time ranges.
                    times_sched = [element[0] for element in times]
                    free_time.append([day,self.find_range_differences(time_restraint,times_sched)])

                new_time = []
                #print(new_time)

                # We find the first occurance of the required days in a row that can be scheduled.
                diff_in_classes = len(dates)-total_classes
                for i in range(diff_in_classes):

                    new_time = free_time[i][1]

                    for j in range(i,i+total_classes):

                        new_time = self.find_range_overlaps(new_time,free_time[j+1][1])
                        # {i: dict_combined[classroom][i] for i in keys_sort}

                    if new_time:
                        times_to_schedule.append([[[free_time[x][0]] for x in range(i,j)],classroom,new_time])
                        able_to_schedule = 1

                        break

            print(times_to_schedule)
            # Jesus fucking christ
            # Ok, need to add functionality to be able to check schedule (cross referencing
            # classroom times ofc) for the soonest n days in a row that the days can be scheduing
            # where n = total_classes (total number of lecture days).
            # This script, at the moment, checks every single day of the term.

            # Do stuff here

    def schedule_all(self,highpop_first = 0):
        leftover_cohorts = []
        all_cohorts = []
        days = []

        for program in programs:
            #print(program.core)
            if (program.core == 1):
                days = ["Monday", "Wednesday"]
            else:
                days = ["Tuesday", "Thursday"]

            for i in range(3): # 3 term sections
                if (not program.core): break

                # Combine mon-wed or tues-thurs into one group of dates
                classroom_dates = self.combine_dates(days)
                possible_times = self.calculate_space(program.populations[i],program.courselist[i],classroom_dates)
                '''
                for courses in program.courselist[i]:
                    
                    # We schedule cohorts for one term at a time.
                    # these courses cannot run at the same time as each other PER cohort
                    # so we loop, reducing the population each time?
                    limitations = []
                    for course in courses:
                        time,classroom = self.check_availability(course,days)
                        self.insert_class(course.course_id,time,classroom,days,limitations)
                        limitations.append([time, time+course.lecture_duration])
                '''

        print()

    def schedule_all_highpop_first():
        print()

    #def add_course(self, ):

    #def check_availability(self, ):

newschedule = Schedule(programs, classrooms)
newschedule.schedule_all()
