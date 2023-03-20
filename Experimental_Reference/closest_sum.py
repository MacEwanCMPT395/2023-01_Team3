''' 
EXPLANATION OF CODE

So, currently, our classrooms have a limited capacity. This capacity is affected by both the hours
of the classes and the populations of the classes. This means the actual capacity is calculated
by hours available in classrooms and by the students needed in them. For example:
We have a class that is (ideally) taught on Mon Wed. In the 2023 semester, there's a total
of 25 classes (I checked the academic calendar and did the calculations). So, if we
have for each class, about 9 hours of available class time, and our total population cap
is 244 students, 244*9*25 = 54900 total student hours. The total amount of hours being taught
in the semester is 28874 (aggregate totals of all PCOM students' hours) which means we should have 
enough capacity for the semester.

Using PCom 101 as an example,
You have this course that requires 35 hours of 2 hours classes with 210 students. 
35/2 = 17.5 which we will round up to 18 (could be 19 too). This Means these students
can complete the course in 18 or 19 out of the 25 days in the semester. 
In the bottom, I set the classes to [40,36,36,30,30,24,24,24]*9 which is
the capacities of our individual classrooms times the 9 hours they're available
in the day. In a "python class" format, this would be a bit neater, but for the
sake of reference and simplicity of demonstration, this is how it looks for now.

So, we find the closest sum (with the smallest amount of total numbers in that sum)
that's greater or equal to our target population.
I added in a factor by which the class must abide (i.e. if each class is 1 hour, then
you'd need a factor of two). This makes it easy to expand. Because say we want 30 minute
increments, instead of 9, we'd use 18 and make our factor 4 (so you'd need 4 timeslots
of equal length)

When running this code, you get:

([30, 30, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36], 0)

So, for PCOM 101, for 18 school days (i.e. ~9 weeks), we have 6 sections,
(because our factor of two, we have to include an even number of timeslots).
so 1 section of 30 (2hr), and 5 sections of classes with capacity 36.

There are only a few limitations which we will work out when we expand this project:
    1. This obviously doesn't actually implement classes yet
    2. It doesn't account for the extra classes at the end of the semester (easy
        to work around, we'll do that later)
    3. There's no easy way to manually calculate capacity, however:
        a) This way, we can detect when capacity for the semester is full and
        b) automatically request more classrooms to satisfy this algorithm
'''

from Classes import Classroom as classroom
'''
def even_repetition_count(lst1, lst2,num):
    
    for value in lst2:
        if ((lst1.count(value) % num) != 0):
            #print(lst1.count(value),num)
            return False
        
    return True
'''

def closest_sum(course, numbers, target):

    numbers = sorted(numbers)
    factors = list(set(numbers))
    combinations = []

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            combinations.append(numbers[i:j+1])
    
    closest = None
    closest_diff = None

    for combination in combinations:
        diff = sum(combination) - target

        # skip loop if we can't reach our target
        if (diff < 0):
            continue

        if (closest_diff is None or diff <= closest_diff):
            if (diff == closest_diff):
                if len(combination) < len(closest):
                    closest = combination
                    closest_diff = diff
            else:
                closest = combination
                closest_diff = diff

    return closest,closest_diff

# We would change these values to reflect the same except minus 2 or 3 each.
# So 38, 34, 34, 28, if our capacity target was 2.
# numbers = [40,36,36,30,30,24,24,24]*9

numbers = [38,34,34,28,28,22,22,22]*9
target = 200
factor = 0 # 4 classes in the term
#result = closest_sum(numbers, target,factor)
#print(result)