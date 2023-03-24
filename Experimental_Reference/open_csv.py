import csv
import Classes as classes
import pathlib

# ---------------------------------------------------
# -- Opening file and checking out the course stuff
# ---------------------------------------------------
programs = []
classrooms = []

extra_capacity = 2

filename = str(pathlib.Path(__file__).parent.resolve())+"\\"
filename += "CSV Files\\"
# open the CSV file and create a bunch of Program objects.
with open(filename+"populations.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header
    for row in reader:
        program, core, t1pop, t2pop, t3pop = row
        program = classes.Program(program,int(core),[int(t1pop), int(t2pop), int(t3pop)],[[],[],[]])
        programs.append(program)

# open the CSV file and create a bunch of Course objects, as well as populating the Program list with said classes.
with open(filename+'classes.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header
    for row in reader:
        program, course_id, course_name, term, class_type, prerequisite, transcript_hours, duration, start, end, cap = row

        for item in programs:
            if item.program_id == program:
                classes.add_course(item, course_id, course_name, int(term), int(class_type), prerequisite, float(transcript_hours), float(duration), float(start), float(end), int(cap), program)
                break

# open the CSV file and create a bunch of Course objects, as well as populating the Program list with said classes.
with open(filename+'classrooms.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # skip header
    for row in reader:
        name, classtype, capacity = row
        classroom = classes.Classroom(name,int(capacity)-extra_capacity,int(classtype))
        classrooms.append(classroom)
'''
for i in programs:
    print(i.program_id, i.courselist,i.populations)

'''
