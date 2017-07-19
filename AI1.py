
import os
import random
from msvcrt import getch
file = open("C:\Users\sandesh\Desktop\work\justforfun\data.txt","a")
# we are assuming the user wants to go from (0,0) to (1,0)
def suggestion(steplist):
    file = open("C:\Users\sandesh\Desktop\work\justforfun\data.txt","r")
    idata = ""
    s4 = 0
    s8 = 0
    s6 = 0
    s2 = 0
    for i in steplist:
        idata = idata + "%s"%i
    length = len(idata)
    for line in file:
        if line.startswith(idata):
            s = line[length]
            if s == "4":
                s4 = s4 + 1
            elif s == "8":
                s8 = s8 + 1
            elif s == "6":
                s6 = s6 + 1
            else:
                s2 = s2 + 1
    if s4 > s8 and s4 > s6 and s4 > s2:
        name = "s4"
    elif s8 > s6 and s8 > s2 and s8 > s4:
        name = "s8"
    elif s6 > s2 and s6 > s4 and s6 > s8:
        name = "s6"
    else:
        name = "s2"
    return name
print "You have to go to position (1,0) from position (0,0)"
a = 0
b = 0
c = 1
d = 0
steplist = []
while True:
    # press 8 to go up 4 to go left 6 to go right and 2 to go down
    # user only goes one step at a time

    num_lines = sum(1 for line in open('data.txt'))
    if num_lines > 10:                      # prints the suggestions only if it has more than 10 inputs
        print "Your suggestion is "
        su = suggestion(steplist)
        if su == "s4":
            print 4
        elif su == "s8":
            print 8
        elif su == "s6":
            print 6
        else:
            print 2
    n = int(raw_input("Enter the direction in which you want to go "))
    test = 0
    while test == 0:
        test = 1
        if n == 8:
            b = b + 1
        elif n == 6:
            a = a + 1
        elif n == 2:
            b = b - 1
        elif n == 4:
            a = a - 1
        else:
            test = 0
            print "You did not enter a valid direction"
    steplist.append(n)
    print "You are now at (%s,%s)"%(a,b)
    if ((a == c) and (b == d)):
        print "You are at the destination"
        if(os.path.getsize("data.txt") > 0):
            file.write("\n")
        for i in steplist:
            file.write("%s"%i)
        file.close()
        break
    
    
