#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Globally Usable System Libraries
from copy import deepcopy
from os.path import exists

#Self Created Libraries to Read Values and Compare Values.
from myCSVOperations import readColumn
from isSame import isSame

#Self Created ictionaries Mapping the Roll Numbers to Names as per College Sheets
from BE_A import BE_A
from BE_B import BE_B


# In[2]:


#Pretty Printing Dicitionary
def prettyPrint(data:dict):
    print("_"*40)
    for val in data:
        print(f'{val:30} ==> {data[val]}')


# In[3]:


def markAttendance(attendeeList:str = None):
    #Read the Complete List of all the Students in the Meeting
    if attendeeList == None:
        print("No File Supplied. Usage:\n\n markAttendance(<filename>)")
    if not exists(attendeeList):
        print(f"File {attendeeList} Does not Exist..")
        return
    
    All_Students = readColumn(attendeeList, columnNo=1, skipRows=2)
    
    #Sorting It
    All_Students.sort()
    
    print(f"{attendeeList}\n\t Total Students Present : {len(All_Students)}")

    #Mark all students as Absent.
    #If a Student is Present then Remove from the List
    BE_A_ABSENT = deepcopy(BE_A)
    BE_B_ABSENT = deepcopy(BE_B)

    # All the Students who have Logged in from
    # some other Account, as well as the Candidates Not in the Provided Lists.
    BE_Unidentified = []
    
    def checkStudent(attendee:str, division:dict):
        for student in division:
            similarity = isSame(student, attendee)
            if similarity == 'YES':
                return student
        
        return "NOTFOUND"
    
    #Traverse through all the meeting Attendee Names
    for presentStudent in All_Students:
        #found flag to indicate if a student is already found in one class
        found = False
        
        #Check every Student in Class A
        student = checkStudent(presentStudent, BE_A)
        if student != "NOTFOUND":
            if student in BE_A_ABSENT:
                BE_A_ABSENT.pop(student)
            found = True
        
        #Check every Student in Class B
        student = checkStudent(presentStudent, BE_B)
        if student != "NOTFOUND":
            if student in BE_B_ABSENT:
                BE_B_ABSENT.pop(student)
            found = True

        if not found:
            BE_Unidentified.append(presentStudent)
    
    
    print("\n\n*************** ABSENT *****************")
    print("\n                 BE A")
    prettyPrint(BE_A_ABSENT)
    print("\n\n                 BE B")
    prettyPrint(BE_B_ABSENT)
    
    print("\n\n************ UNIDENTIFIED **************\n")

    for stud in BE_Unidentified:
        print(stud)


# In[4]:


markAttendance('Class Attendances/Class List (2020-07-22) (1).csv')


# In[8]:


len(BE_A) + len(BE_B)


# In[ ]:




