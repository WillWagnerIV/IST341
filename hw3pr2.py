# IST341, hw3pr2
# Filename: hw3pr2.py
# Name: Will Wagner
# Problem description: Sleepwalking student

import sys
sys.setrecursionlimit(50000) # extra stack room

import time
from random import *


# example "random" code from class

# def guess(hidden):
#     """A number-guessing example
#        to highlight using the
#        random library
#     """
#     comp_guess = choice(range(100)) # 0 to 99, incl.
#     if comp_guess == hidden:
#         print("I got it! It was", comp_guess)
#         print("Total guesses:")
#         return 1

#     else:
#         print("Aargh. I guessed", comp_guess)
#         time.sleep(0.1)
#         return 1 + guess(hidden)


def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return int(choice([-1, 1]))

def rwpos(start, nsteps):
    """ returns swpos: a random position after being given 2 arguments: 
    start = start postion 
    nsteps = number of steps in a random direction one at a time
    """

    print("start is: ",start)
    
    if nsteps == 0:
        return start
    
    else:
        rwpos(start+rs(), nsteps-1)
    return

def rwsteps(start, low, hi):
    """ Draws a sleepwalker randomly moving
        takes arguments:
        start = starting position
        low = left wall
        hi = right wall
    """

    leftSpaces = start - low
    rightSpaces = hi - start
    if rs() > 0:
        char = ":)"
        step = 1
    else:
        char = "(:"
        step = -1

    print("XXX","_"*leftSpaces,char,"_"*rightSpaces,"XXX")
    
    if start == low:
        return

    elif start == hi:
        jumpOffCliff(leftSpaces,rightSpaces)       # IF the guy gets to the right side jump over the edge!
        return

    rwsteps(start+step, low, hi)

    return

##############  Some goofyness if the guy gets to the RIGHT SIDE

def jumpOffCliff(leftSpaces,rightSpaces):  # Some Goofyness!!
    char =":)"
    print("XXX","_"*(leftSpaces + rightSpaces+4),"XXX",char)
    print("XXX","_"*(leftSpaces + rightSpaces+4),"XXX ",char)
    print("XXX","_"*(leftSpaces + rightSpaces+4),"XXX  ",char," I'm Free!")
    time.sleep(1.0)      # and then sleep for 0.1 seconds
    char =":("
    print("XXX","_"*(leftSpaces + rightSpaces+4),"XXX  ",char," Aarrgh!")

    for x in range(1,10): 
        print("XXX","_"*(leftSpaces + rightSpaces+4),"XXX  ",char)

    print("XXX","_"*(leftSpaces + rightSpaces+4),"XXX  ","SPLAT!")

    return

def rwposPlain(start, nsteps):
    """ 
        Returns the man's position after being given 2 arguments: 
        start = start postion 
        nsteps = number of steps in a random direction one at a time
    """
    
    if nsteps == 0:
        #print(" Final Position is: ",start)
        return start    
    else:
        return rwposPlain(start+rs(), nsteps-1)
    
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

def ave_signed_displacement(numtrials):
    """
        Returns the Average Signed Displacement. numtrials = number of iterations of 100 steps each
    """

    LC = [rwposPlain(0, 100) for x in range(numtrials)]
        
    return sum(LC) / len(LC)


def ave_squared_displacement(numtrials):
    """
        Returns the Average Squared Displacement. numtrials = number of iterations of 100 steps each
    """

    LC = [(rwposPlain(0, 100)**2) for x in range(numtrials)]
        
    return sum(LC) / len(LC)



#
# Main Area to investigate questions
#

"""
     To compute the average signed displacement for
     a random walker after 100 random steps, I created a Main Area
     to ask the user for appropriate input and return the requested
     information.

     Average Displacement is calculated by asking for a number of
     iterations (n), then storing each answer in a list,
     and finally returning the avg number in the list.

=========    Sample output:     =========

In [139]: run hw3pr2.py
Average Signed Displacement and Average Squared Displacement
How many iterations? 5
Average Signed Displacement:  2.8
Average Squared Displacement:  17.6
Again y/n)y
Average Signed Displacement and Average Squared Displacement
How many iterations? 5
Average Signed Displacement:  8.4
Average Squared Displacement:  48.8
Again y/n)y
Average Signed Displacement and Average Squared Displacement
How many iterations? 10
Average Signed Displacement:  -1.0
Average Squared Displacement:  116.4
Again y/n)y
Average Signed Displacement and Average Squared Displacement
How many iterations? 10000
Average Signed Displacement:  0.165
Average Squared Displacement:  98.2652
Again y/n)


"""


#######  DISREGARD FROM HERE DOWN - I WAS EXPERIMENTING   #####


# def endLoop():
#     """ Just a way to end the program """
#     print("Goodbye.")



# def mainLoop():

#     print()
#     print()
#     print("*** MAIN MENU ***")
#     print("=================")
#     print("1 - Sleepwalker")
#     print("2 - Investigation")
#     print("3 - Exit")


#     choice = input("Choice:  ")

#     if choice == "1":
#         start=int(input("Start:  "))
#         low= int(input("Low:  "))
#         hi = int(input("Hi:  "))
#         rwsteps(start, low, hi)

#     if choice == "2":
#         print("Average Signed Displacement and Average Squared Displacement")
#         n = int(input("How many iterations? "))

#         print("Average Signed Displacement: ", ave_signed_displacement(n))
#         print("Average Squared Displacement: ", ave_squared_displacement(n))
#         mainLoop()
    
#     if choice =="3":
#         endLoop()


# mainLoop()

