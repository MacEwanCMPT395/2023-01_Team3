'''
Author: Sage Jurr
Date: Jan.29,2023
Purpose: define Program class
'''

class Program:
    '''
    Note: Internally we will treat core courses as a program (program = core)
    '''
    
    # Name is the name of the program
    
    # coursesOffered will be a list of the courses offered in the program
 
    # coursesToComplete will be a list of courses needed to Complete the program
    
    # prereq will be a list of prerequisites needed to take the program
    
    
    def __init__(self, name, coursesOffered, coursesToComplete, prereq):
        self.name = name
        self.coursesOffered = coursesOffered
        self.coursesToComplete = coursesToComplete
        self.prereq = prereq
        
        
def tests():
    PM = Program('Project Management (PM)', ['PRDV0201', 'PRDV0202', 'PRDV0203','PRDV0204', 'PRDV0205', 'PCOM0130', 'PRDV0206', 'PRDV0207', 'PCOM0131'], ['PRDV0201', 'PRDV0202', 'PRDV0203','PRDV0204', 'PRDV0205', 'PCOM0130', 'PRDV0206', 'PRDV0207', 'PCOM0131'], ['None'])
    
    corePCOM = Program('Professional Communication (PCOM)', ['PCOM0101', 'PCOM0105', 'PCOM0107', 'CMSK0233', 'CMSK0235', 'PCOM0102', 'PCOM0201', 'PCOM0108', 'PCOM0202', 'PCOM0103', 'PCOM0109'], ['PCOM0101', 'PCOM0105', 'PCOM0107', 'CMSK0233', 'CMSK0235', 'PCOM0102', 'PCOM0201', 'PCOM0108', 'PCOM0202', 'PCOM0103', 'PCOM0109'], ['None'] )
    
    print('The program is: ', PM.name)
    print('The courses offered in this program are: ')
    for i in range(len(PM.coursesOffered)):
        print(PM.coursesOffered[i])
        
    print()
        
    print('The courses required to complete the program are: ')
    for i in range(len(PM.coursesToComplete)):
        print(PM.coursesToComplete[i])   
        
    print()    
        
    print('The courses required to take this program are: ')
    for i in range(len(PM.prereq)):
        print(PM.prereq[i])
        
    print()
    
    print('The program is: ', corePCOM.name)
    print('The courses offered in this program are: ')
    for i in range(len(corePCOM.coursesOffered)):
        print(corePCOM.coursesOffered[i])
        
    print()
        
    print('The courses required to complete the program are: ')
    for i in range(len(corePCOM.coursesToComplete)):
        print(corePCOM.coursesToComplete[i])   
        
    print()    
        
    print('The courses required to take this program are: ')
    for i in range(len(corePCOM.prereq)):
        print(corePCOM.prereq[i])
        
    print()    

#tests()