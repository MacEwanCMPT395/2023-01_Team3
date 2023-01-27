## How the program should behave

* Seven different school programs
  * Limited number of classrooms to divide between the 7 of the programs.
    * There are various formats and patters for lectures:
      * Lecture Time:
      * 3-hours lectures once a week.
      * 1.5-hour lecture twice a week.
      * 2-hour lecture once a week.
      * Etc…
  * Lectures must be scheduled from 8:00 am to 5:00 pm, from Monday to Thursday, except the computer programming one which is 430-8 iirc
    * Therefore, we need to have a way to specify limitations for the time a program can run
  * There are two groups of courses:
    * Core courses and Program Specific Courses (see document “SCE_ProgramsCourses.xlsx”).
    * Core courses are required for all students while program specific courses are specific to each program
    * The software should optimize the scheduling and sequence of courses and the use of physical resources (i.e., classrooms and labs available) to maximize the number of students that can be registered each term
      * This should be fairly easy to do 
    * The students must not have more than 1.5 hrs. gaps

## So, what do we need to make this program??
* First, we need a class and schedule editor
  * Edit the programs' classes
  * To specify class times, restrictions etc
  * Specify order, unavailable days, holidays, etc

## Pseudocode?
* Open class file
* Sort data into dictionaries
  * Programs
    * Program A
      * Student Count
    * Program B
    * 
  * Classes
    * Class A
      * Class Length (per meeting, e.g. 2hrs)
      * Total Class Length (e.g. 35 hours) (we should have the class length plus the length of one class when we use the data. Or let the user specify this
      * Requirements
  * Schedule Stuff (Semester info)
    * Unavailable Days (holidays)
    * Semester Start and Finish

Things to Think about
* How to we determine how many classrooms we need?
* How to most efficiently use classrooms? (I have this figured out)
* How will we edit the classes, and determine order, etc?
* What will our for loops look like?
* How will we determine how to place a class?
  * The class must be on certain days?

Programming Order
* We should make the algorithms for the data first
* Like efficiently placing classes, etc.
* We are not sure when we will be given the csv data so we should create our own data for now. Opening and dispersing the data into lists will be the easy part.
  * If we make our program flexible, this shouldn't be an issue anyways.

Data we need to make before the CSV is given to us to determine class order and whatnot
* Schedule information


## Editor Approach:
* Semester
  * Start and End Semester Dates
  * Holiday and Cancellation Dates
* Weekly
  * Weekly restrictions (only certain days, or NOT on only certain days)
* Daily
* Half Hour Increments
* Hourly Limitations (i.e. before or after a certain time of day)
  * These limitations can be given by the program the class is a part of.
