# days is a list of teachable days.
from Time_Stuff import days
print(days)

import Classes as classes
from open_csv import programs, classrooms

def takeSecond(elem):
    return elem[1]

def sum_population(combination):
    total = 0
    for classroom in combination:
        total += classroom.capacity -1
        
def possible_times(room_hrs_times, class_length):

    return_data = []
    time_starts = {}
    for item in room_hrs_times:
        classroom, slots, dates = item
        
        time_starts[classroom] = []
        slot_factor = 0
        
        for time_ranges in slots:
            start_time = time_ranges[0]
            end_time = time_ranges[1]
            
            while (end_time - class_length) >= start_time:
                time_starts[classroom].append(end_time - class_length)
                end_time -= class_length
                slot_factor += 1
            
        for i in range(slot_factor):
            return_data.append(classroom)
            #print(time_starts)
    return return_data,time_starts
    
def closest_sum(room_hrs_times, target,class_length, extra_classes = []):
    target+= 2
    classrooms,time_starts = possible_times(room_hrs_times,class_length)

    n = len(classrooms)
    dp = [[0] * (target + max([c.capacity for c in classrooms]) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(len(dp[0])):
            dp[i][w] = dp[i - 1][w]
            if classrooms[i - 1].capacity <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - classrooms[i - 1].capacity] + classrooms[i - 1].capacity)

    target_weight = target + 1
    while dp[n][target_weight] == 0 and target_weight < len(dp[0]) - 1:
        target_weight += 1

    items = []
    i = n
    while i > 0 and target_weight > 0:
        if dp[i][target_weight] != dp[i - 1][target_weight]:
            items.append(classrooms[i - 1])
            target_weight -= classrooms[i - 1].capacity
        i -= 1
    
    total_weight = sum(obj.capacity for obj in items)
    weight_diff = total_weight - target
    
    return_result = []
    for classroom in items:
        for c_room, times in time_starts.items():
            if c_room == classroom:
                return_result.append((classroom,time_starts[classroom].pop(0)))
    
    total_weight2 = total_weight
    weight_diff2 = weight_diff
    
    required_classes = return_result + extra_classes
    if (weight_diff < 0):
        total_weight2, required_classes, weight_diff2 = closest_sum(room_hrs_times, -weight_diff,class_length,required_classes)[1]

    #print(total_weight,total_weight2)
    
    return (total_weight, return_result, weight_diff),(total_weight2, required_classes, weight_diff2)
        

class Schedule:
    def __init__(self, programs, classrooms):
        self.programs = programs
        self.classrooms = classrooms

        # insert online classroom
        
        self.classrooms.append(classes.Classroom("Virtual",-1,2))

        self.classrooms.append(classes.Classroom("GHOST_Lecture",-1,2))
        self.classrooms.append(classes.Classroom("GHOST_Lab",-1,2))
        
        self._schedule = {"Monday":[],
                         "Tuesday":[],
                         "Wednesday":[],
                         "Thursday":[],
                         "Virtual":[]}

        # for now no need for friday and saturday, but can easily be added.
        self.schedule = {classroom:dict(days) for classroom in classrooms}

        #print(self.schedule)

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
        num_classes_in_semester = 0
        for classroom in (self.classrooms):
            dict_combined[classroom] = {}
            for dow in days: #dow = day of week
                for dates, times in self.schedule[classroom][dow].items():
                    if dates in dict_combined[classroom]:
                        dict_combined[classroom][dates].append(times)
                    else:
                        dict_combined[classroom][dates] = times

                    num_classes_in_semester+=1

            # Sort our dictionary.
            keys_sort = list(dict_combined[classroom].keys())
            keys_sort.sort()

            sorted_dict = {i: dict_combined[classroom][i] for i in keys_sort}

            dict_combined[classroom] = sorted_dict

        return num_classes_in_semester,dict_combined

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

    def find_range_overlaps(self, range_set1, range_set2, min_diff):
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

                    if min_diff <= (overlap_end-overlap_start):
                        overlaps.append((overlap_start, overlap_end))

        return overlaps

    def find_valid_classrooms(self,course,classes_w_dates):
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

                for classroom,dates in classes_w_dates.items():
                    if classroom.lab_room == i:
                        real_dates[classroom] = dates
                break

        return real_dates
    
    def create_ghost_class(self):
        print("TODO")
        

    def create_ghost_classes(self, c1, c2):
        
        l1 = len(c1)
        l2 = len(c2)
        print(c1)
        # easily remove dupes by list comprehension and adding to a set, convert back.
        setofplaces = {x[0] for x in c1}
        factor = l2 / l1
        factor = (factor > int(factor)) and int(factor) or int(factor-1)
        newlist = []
        for i in list(setofplaces):
            newlist += [i]*factor
        print(newlist)
        
        new_class = self.create_ghost_class()
        self.schedule
        
    def find_schedule_single_class(self, real_dates, time_restraint, total_classes, lecture_length, population):

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

            # times to schedule is possible times to schedule for valid classrooms for ONE and only ONE course.
            # This finds the overlap that is consistent with a given hour range so the class can be
            # scheduled at the same time every day.

        times_to_schedule = []

        # dummy variable so far
        able_to_schedule = 0

        for classroom, dates in real_dates.items():
            free_time = []
            for day, times in dates.items():
                # Should create a list of lists or something of that nature. [[time range], class/cohort]
                # doing element[0] should copy just the time ranges.
                times_sched = [element[0] for element in times]
                free_time.append([day, self.find_range_differences(time_restraint, times_sched)])

            # we're still in the for loop. new_time is the
            new_time = []

            # We find the first occurance of the required days in a row that can be scheduled. So, if a class runs for
            # 35 hours and is 1.5 hours per lecture, find the first (35/1.5) days in a row.
            diff_in_classes = len(dates) - total_classes
            for i in range(diff_in_classes or 1):

                new_time = free_time[i][1]

                # This loop finds the overlaps of free times between different days
                # and puts them in new_time.
                jrange = min(total_classes+1, len(free_time) - 1)
                maxj = 0
                for j in range(i, i + jrange):

                    new_time = self.find_range_overlaps(new_time, free_time[j + 1][1], lecture_length)
                    maxj = j
                    # {i: dict_combined[classroom][i] for i in keys_sort}

                if new_time:
                    # This loop gives the following: [Classroom, [list of free times], [date range]]
                    times_to_schedule.append([classroom, new_time, [free_time[x][0] for x in range(i, maxj)]])
                    able_to_schedule = 1

                    break
        
        #print(times_to_schedule)
        class_distribution = closest_sum(times_to_schedule, population, lecture_length)
        c1,c2 = class_distribution
        
        if (c1[0] != c2[0]):
            self.create_ghost_classes(c1[1],c2[1])
        
        return times_to_schedule

    def calculate_space(self,courses,population,classroom_dates):
        
        num_classes_in_semester, classes_w_dates = classroom_dates

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
            
            
            real_dates = self.find_valid_classrooms(course,classes_w_dates)
            
            # grace = the number of extra classes to be scheduled. If we have room, add one.
            grace = 1

            total_classes = (course.transcript_hours) // duration
            if (total_classes > num_classes_in_semester):
                print("too many hours for date range")

            total_classes = int((total_classes+grace <= num_classes_in_semester) and total_classes + grace or total_classes)
            
            times_to_schedule = self.find_schedule_single_class(real_dates, time_restraint, total_classes, course.lecture_duration,population)

            #print(times_to_schedule)
            #ideal_times = ideal_class_distribution()

    def schedule_all(self,highpop_first = 0):
        leftover_cohorts = []
        all_cohorts = []
        days = []
        
        cohorts_populations = []
        programs = self.programs

        for program in programs:
            for i in range(3): # 3 term sections
                cohorts_populations.append((program.courselist[i],program.populations[i],program.core))

        cohorts_populations.sort(key=takeSecond)

        for termclasses in cohorts_populations:
            courses, population, core = termclasses

            if (not core): continue

            if (core == 1):
                days = ["Monday", "Wednesday"]
            else:
                days = ["Tuesday", "Thursday"]

            # Combine mon-wed or tues-thurs into one group of dates
            classroom_dates = self.combine_dates(days)
            possible_times = self.calculate_space(courses,population,classroom_dates)


            for i in range(3): # 3 term sections

                # This is just here because we have no data for non-core classes yet
                
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


        return

    def schedule_all_highpop_first():
        print()

    #def add_course(self, ):

    #def check_availability(self, ):

newschedule = Schedule(programs, classrooms)
newschedule.schedule_all()
