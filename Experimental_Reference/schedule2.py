# days is a list of teachable days.
import datetime
from Time_Stuff import days
import copy
#print(days)

import Classes as classes
from open_csv import programs, classrooms

def takeSecond(elem):
    return elem[1]
        
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

def add_times(items,time_starts):
    return_result = []
    for classroom in items:
        for c_room, times in time_starts.items():
            if c_room == classroom:
                return_result.append((classroom,time_starts[classroom].pop(0)))

    return return_result

def subset_sum_with_reconstruction(items, max_weight):
    n = len(items)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
    for j in range(1, max_weight + 1):
        dp[0][j] = float('inf')

    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if items[i - 1].capacity > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - items[i - 1].capacity] + 1)

    if dp[n][max_weight] == float('inf'):
        return None

    # Reconstructing the smallest subset of items
    subset = []
    i, j = n, max_weight
    while i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            i -= 1
        else:
            subset.append(items[i - 1])
            j -= items[i - 1].capacity
            i -= 1

    return subset

def get_real_time(items, target):

    maximum = max(item.capacity for item in items)
    for i in range(maximum):
        sum_classes = subset_sum_with_reconstruction(items, target+i)
        if sum_classes != None:
            return sum_classes

    return None # wtf

def closest_sum(room_hrs_times, target,class_length, extra_classes = [],increment = 0):
    classrooms,time_starts = possible_times(room_hrs_times,class_length)

    real_schedule = []
    ghost_required  = 0

    maxsum = sum(item.capacity for item in classrooms)
    if (target > maxsum):

        real_schedule = add_times(classrooms,time_starts)
        ghost_required = 3
    else:
        min_sum = get_real_time(classrooms,target)
        real_schedule = add_times(min_sum,time_starts)

    return real_schedule,ghost_required

def pretty_print_nested_dict(dictionary, indent=0):
    for key, value in dictionary.items():
        print(' ' * indent + str(key))
        if isinstance(value, dict):
            pretty_print_nested_dict(value, indent + 4)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    pretty_print_nested_dict(item, indent + 4)
                else:
                    print(' ' * (indent + 4) + str(item))
        else:
            print(' ' * (indent + 4) + str(value))


# ------------------------------------------------------------------#
# MAIN MAIN MAIN MAIN MAIN -----------------------------------------#
# ------------------------------------------------------------------#
class Schedule:
    def __init__(self, programs, classrooms):
        self.programs = programs
        self.classrooms = classrooms

        # insert online classroom
        # infinite capacity for online classrooms
        self.classrooms.append(classes.Classroom("Online",999,2))

        self._schedule = {"Monday":[],
                         "Tuesday":[],
                         "Wednesday":[],
                         "Thursday":[],
                         "Virtual":[]}

        # for now no need for friday and saturday, but can easily be added.

        self.schedule = {classroom:copy.deepcopy(days) for classroom in classrooms}
        self.scheduled_classes = {}
        self.failed = []
        self.courselist = []
        self.virtual_courses = []

        self.raw_schedule = {}

        #self.print_schedule()
        
    def get_raw_schedule(self):
        return self.combine_dates(["Monday", "Tuesday", "Wednesday", "Thursday"])[1]

    def combine_dates(self, days):

        # This would work for mon, wed, fri classes.
        dict_combined = {}
        num_classes_in_semester = 0
        for classroom in (self.classrooms):
            dict_combined[classroom] = {}
            for dow in days: #dow = day of week
                for dates, times in self.schedule[classroom][dow].items():
                    if dates in dict_combined[classroom]:
                        dict_combined[classroom][copy.deepcopy(dates)].append(times)
                    else:
                        dict_combined[classroom][copy.deepcopy(dates)] = times

                    

            # Sort our dictionary.
            keys_sort = list(dict_combined[classroom].keys())
            num_classes_in_semester = len(keys_sort)
            keys_sort.sort()

            sorted_dict = {i: dict_combined[classroom][i] for i in keys_sort}

            dict_combined[classroom] = sorted_dict

        return num_classes_in_semester,dict_combined
    
    def print_schedule(self):
        pretty_print_nested_dict(self.schedule)
        #print(self.schedule)
        return None
    
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
        start = min_max[0]

        for data_range in data_ranges:
            if start < data_range[0]:
                differences.append((start, data_range[0]))
            start = max(start, data_range[1])

        if start < min_max[1]:
            differences.append((start, min_max[1]))
        
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
        for i in range(4):
            if (course.class_type == i+1):

                for classroom,dates in classes_w_dates.items():
                    if classroom.c_type == i:
                        real_dates[classroom] = dates
                        
                break
        
        return real_dates
    
    def capstone_remove_dates(self, data, course_length):
        new_data = {}
        for outer_key in data:
            inner_dict = data[outer_key]
            all_dates = list(inner_dict.keys())
            semester_length = len(all_dates)
            half_term = semester_length // 2
            earliest_start = semester_length - course_length

            start_index = min(half_term, earliest_start)
            remaining_dates = all_dates[start_index:]
            new_data[outer_key] = {date: inner_dict[date] for date in remaining_dates}

        return new_data

    def find_schedule_single_class(self, real_dates, time_restraint, total_classes, lecture_length, population, illegal_times):

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

        possible_times_to_schedule = []

        # dummy variable so far
        able_to_schedule = 0

        for classroom, dates in real_dates.items():

            #print(dates)
            free_time = []
            for day, times in dates.items():

                # Should create a list of lists or something of that nature. [[time range], class/cohort]
                # doing element[0] should copy just the time ranges.



                times_sched = [element[0] for element in times]

                if illegal_times:
                    times_sched = times_sched + illegal_times[0][0]
                
                free_time.append([day, self.find_range_differences(time_restraint, times_sched)])

            # we're still in the for loop. new_time is the time ranges for this 
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

                # new_time in this loop references itself to find a required overlap in free time
                for j in range(i, i + jrange):
                    new_time = self.find_range_overlaps(new_time, free_time[min(j + 1, len(free_time)-1)][1], lecture_length)
                    maxj = j
                    # {i: dict_combined[classroom][i] for i in keys_sort}

                if new_time:
                    # This loop gives the following: [Classroom, [list of free times], [date range]]
                    schedule_dates = [free_time[x][0] for x in range(i, maxj)]
                    possible_times_to_schedule.append([classroom, new_time, schedule_dates])
                    able_to_schedule = 1

                    break


        if not able_to_schedule:
            return [],[],2
    
        class_distribution, ghost = closest_sum(possible_times_to_schedule, population, lecture_length)

        return class_distribution, copy.deepcopy(schedule_dates), ghost
    

        

    def schedule_section(self, course, times_to_schedule,schedule_dates):
        
        schedule = self.schedule
        i=0
        for room,time in times_to_schedule:
            
            i+=1 # i is the section number for the class!!!!
            for day in schedule_dates:
                dow = day.strftime("%A")
                toadd = [(time, time+course.lecture_duration),course, i]
                schedule[room][copy.deepcopy(dow)][copy.deepcopy(day)].append(toadd)

        course.last_day = schedule_dates[-1]

    def capstone_remove_dates(self, data, course_length):
        new_data = {}
        for outer_key in data:
            inner_dict = data[outer_key]
            all_dates = list(inner_dict.keys())
            semester_length = len(all_dates)
            half_term = semester_length // 2
            earliest_start = semester_length - course_length

            start_index = min(half_term, earliest_start)
            remaining_dates = all_dates[start_index:]
            new_data[outer_key] = {date: inner_dict[date] for date in remaining_dates}

        return new_data

    def preq_remove_dates(self, data, course_length, course_to_schedule):
        
        latest_date_int = 0
        for course in self.courselist:
            if course.course_id == course_to_schedule.preq:
                latest_date = course.last_day
        
        if not latest_date:
            #print("oh no")
            return None

        new_data = {}
        for outer_key in data:
            inner_dict = data[outer_key]
            all_dates = list(inner_dict.keys())

            latest_date_int = all_dates.index(latest_date)

            remaining_dates = all_dates[latest_date_int:]
            new_data[outer_key] = {date: inner_dict[date] for date in remaining_dates}

        return new_data
    
    def calculate_space(self,courses,population,classroom_dates):
        
        num_classes_in_semester, classes_w_dates = classroom_dates
        #print(num_classes_in_semester)

        #print(classes_w_dates)
        factor = len(courses)
        dateset = False

        # Scheduling within a cohort:
        # Once one class is scheduled, the next 2 cannot
        # be scheduled at the same time
        illegal_times = []

        # Find possible times one course at a time.
        # We then divide these possible times into our cohort.
        for i, course in enumerate(courses):
                
            if course.class_type == 4:
                self.virtual_courses.append(course)
                continue

            duration = course.lecture_duration

            time_restraint = [course.lecture_start_time, course.lecture_end_time]

            real_dates = self.find_valid_classrooms(course, classes_w_dates)
            # grace = the number of extra classes to be scheduled. If we have room, add one.
            grace = 1

            # Is it possible to schedule this many hours in this date range?
            total_classes = (course.transcript_hours) // duration
            if (total_classes > num_classes_in_semester):
                self.failed.append([course,1])
                continue

            # Remake the total classes to add grace if we have room. total_classes is an int.
            total_classes = int((total_classes+grace <= num_classes_in_semester) and total_classes + grace or total_classes)

            # Course cap will determine if we schedule backwards.
            # Schedule backwards = schedule from halfway through the term or
            # the absolute minimum start time (if there's too many hours, say,
            # 20 hours, we will have to start earlier than halfway)
            # Think: (min(half, abs minimum start time))
            # We can calculate and compare the dates.

            if course.cap:
                real_dates = self.capstone_remove_dates(real_dates, total_classes)

            # This will be for prereq checking
            if course.preq:
                dates = self.preq_remove_dates(real_dates, total_classes, course)
                if dates:
                    real_dates = dates

            # failed reasons:   1 = Too many hours for the semester (case above)
            #                   2 = Cannot fit class into schedule
            #                   3 = Could not create enough cohorts due to physical class bottleneck
            times_to_schedule, schedule_dates, failed = self.find_schedule_single_class(real_dates, 
                                                            time_restraint, total_classes, course.lecture_duration,population,
                                                                                                                illegal_times)
            #print(times_to_schedule, "\n\n", schedule_dates,"\n")
            if failed:
                self.failed.append([course,failed])

            # Even if it failed, let's try to add to schedule anyways.
            if times_to_schedule:
                self.schedule_section(course, times_to_schedule, schedule_dates)

            illegal_times.append([list({(x[1], x[1] + course.lecture_duration) for x in times_to_schedule}), schedule_dates])
                
            

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
            
            self.courselist += courses
            
            if (core == 1):
                days = ["Monday", "Wednesday"]
            else:
                days = ["Tuesday", "Thursday"]

            # Combine mon-wed or tues-thurs into one group of dates using the real
            # scheduler.
            classroom_dates = self.combine_dates(days)
            possible_times = self.calculate_space(courses,population,classroom_dates)

        return
    # Generate Out Creates a BROKEN SCHEDULE

    def generate_out(self):
        classes = self.get_raw_schedule()
        week_classes = {}
        for room, data in classes.items():
            counter = 1
            for i, class_date in enumerate(sorted(data.keys())):

                class_times = data[class_date]
                if class_date.weekday() == 0 and i != 0:
                    counter += 1

                week_name = "Week "+str(counter) 

                if week_name not in week_classes:
                    week_classes[week_name] = {}

                class_id = room.classroom_id
                if class_id not in week_classes[week_name]:
                    week_classes[week_name][class_id] = {}
                    week_classes[week_name][class_id]["monday"] = []
                    week_classes[week_name][class_id]["tuesday"] = []
                    week_classes[week_name][class_id]["wednesday"] = []
                    week_classes[week_name][class_id]["thursday"] = []

                for class_time in class_times:
                    start_hour = int(class_time[0][0])
                    start_minute = int((class_time[0][0] - start_hour) * 60)
                    if start_minute == 30:  # handle :30 input
                        start_minute_str = '30'
                    else:
                        start_minute_str = '00'

                    end_hour = int(class_time[0][1])
                    end_minute = int((class_time[0][1] - end_hour) * 60)
                    if end_minute == 30:  # handle :30 input
                        end_minute_str = '30'
                    else:
                        end_minute_str = '00'

                    start_time = datetime.time(hour=start_hour, minute=start_minute).strftime('%I:%M %p')
                    end_time = datetime.time(hour=end_hour, minute=end_minute).strftime('%I:%M %p')
                    course = class_time[1].course_id + " - AS" + "{:02d}".format(class_time[2])
                    week_classes[week_name][class_id]["monday"].append({"course": course, "start_time": start_time, "end_time": end_time})

        return week_classes

#newschedule = Schedule(programs, classrooms)
#newschedule.schedule_all()
#pretty_print_nested_dict(newschedule.generate_out())


