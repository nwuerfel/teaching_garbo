## Plot it ##
##A stupid program to display grades
##and take averages so I dont fuck my
##kids over too bad when I grade too harshly
#
#
# N. Wuerfel 2017 Umich goblu
#
# revised by mr manhimself 2018
# started git Feb1 2018 
# ~~~~AP~~~~

helpMessage='biteme'
studentFileMark='.std'

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import subprocess as sp
import getopt
import sys


# displayHub is the main gui for interaction with data and lists and shit
def displayHub(data):
    print('underconstruction')



# gets lists of students from all courses in given homedir
# returns as list lists of following format:
##
## [[Last','First','LastinitialFirstinital']...]
def getStudents(homedir):

    # change with file spec
    numStudentField = 3

    # sanitize homedir
    if homedir=='':
        # TODO FAIL GRACEFULLY
        print('I assume you meant the current directory')
        homedir = '.'
    if not homedir.endswith('/'):
        homedir = homedir+'/'

    # each entry is one class worth of students
    allStudents = []

    # return lists of students for each course    
    # each line is student csv goes as
    # LAST,FIRST,LF,etc.....
    for fileName in sp.check_output(['ls',homedir]).split():
        if not fileName.endswith(studentFileMark):
            print 'DID NOT ACCEPT:'
            print fileName
            continue
        try: 
            # clean up file
            with open(homedir+fileName,'r+') as fp:
                studentList = fp.readlines()
                for idx in range(len(studentList)):
                    if studentList[idx].endswith('\n'):
                        studentList[idx]=studentList[idx][:-1]
                    studentList[idx]=studentList[idx].split(',')
                    # note to fix file 
                    if len(studentList[idx]) != numStudentField:
                        print'Student list thing is weird'
                        print(studentList[idx]) 
                    # ask for approval to change file
                        #TODO
                    # for now i guess ill just die
                        quit('bleh')
                allStudents.append(studentList)
                    
                # check for and resolve redundancies
                # clunky to double iterate but idk how to better in this fucking
                # script bullshit language why isn't this in FORTRAN anyway?
            
                # WHY DOESNT THIS FUCKING SHIT SUPPORT POINTERS MOTHERFUCKER I
                # HAVE TO DO INEFFICIENT BULLSHIT TO GET THESE FUCKING GARBO
                # INDEXES TO CHANGE VALUES WHILE ITERATING INSTEAD OF JUST
                # HAVING A FUCKING POINTER 
                for idx in range(len(studentList)):
                    for jdx in range(len([])):
                        if jdx==idk:
                            continue
                        if studentList[idx][2]==studentList[jdx][2]:
                            print('HOLY SHIT ITS REDUNDANCY, fix these initials son\n')
                            print('Earlier:\n')
                            print(studentList[idx]) 
                            print('LADder:\n')
                            print(studentList[jdx])
                        # i just die now 
                        #TODO A GRACEFUL DEATH!
                            quit()
                            

                # double check user's dumb ass 
                # currently just prevents reusing initials
        except IOError:
            print('what did u do to the files, stupid')
            print(fp)
            
            #a = sp.call('clear')
            #quit('BAD JOB, are you happy?')
    return(allStudents)

def plotIt(A,totalPossible): 

    
    # A is a vector of scores 

    #convert to percents
    B = [float(a)/totalPossible for a in A]
    #plt.plot(A,range(len(A)))    
    plt.hist(B,8,normed=1) 

    # draw gaussian along with it
    mean = sum(B)/float(len(B))
    std = np.std(B)
    x = np.linspace(mean-3*std, mean+3*std, 100)
    plt.plot(x,mlab.normpdf(x,mean,std))
    plt.show()
    

def main(argv):

    # UI bullshit
    defaultDir = '.'

    try:
        opts, args = getopt.getopt(argv, "hi:o:")    
    except getopt.GetoptError:
        print helpMessage
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print helpMessage
            sys.exit()
        elif opt == '-i':
            inFileName =str(arg)
        elif opt == '-o':
            arg = input('lab number: ')
            outFileName = '../grades/lab' + str(arg) + '.grd'

    # sanitization done in function
    myStudents = getStudents(inFileName)
    
    numClasses = len(myStudents)

    totalPossible = float(raw_input("total points possible? "))

    for classRoom in myStudents:

        # will be depricated but its late 
        # horribly assumes num-alphabetic ordering
        className = '15'+str(myStudents.index(classRoom)+1)

        # NOT SAFE(?) FIX PLS 
        grades = input('grades for' + className + '? ')
        if type(grades) is int:
            grades = [grades]
 
        #grades = [float(a) for a in raw_input('grades for' + className + '? ')]
       
    plotIt(grades,totalPossible)
        




if __name__ =="__main__":
    main(sys.argv[1:])
