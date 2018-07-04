#
# hw9pr3.py - Pi from Pie
#
# Name: Will Wagner
# IST341 3/4/18
#

import random
import math

def throwDart():
    """ 
        Function returns True if the dart is within the circle
    """

    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    
    # a2 + b2 = c2
    # print(math.sqrt((x**2)+(y**2)))

    return math.sqrt((x*x)+(y*y)) < 1

def forPi(n):
    """ 
        Function accepts an integer and will return the final
        estimate of Pi after n throws
    """
    cirHits = 0
    sqHits = 0

    for throws in range(n+1):

        if throwDart():
            cirHits += 1

        estPi = (( 4 * cirHits ) / (throws+1))

        print(cirHits,"hits out of",throws+1,"throws so that pi is:",estPi)

    return estPi

def whilePi(error):
    """
        Will throw darts until the estimated value of Pi is within 'error' range
        of real Pi
    """

    throws = 0
    cirHits = 0
    sqHits = 0
    missedBy = 10

    while missedBy > error:

        throws += 1

        if throwDart():
            cirHits += 1

        estPi = (( 4 * cirHits ) / (throws))

        print(cirHits,"hits out of",throws,"throws so that pi is:",estPi)
        missedBy = abs(math.pi - estPi)
        # print(missedBy)

        if throws == 50000: # Breaks after 50000 tries
            print("Stopped after 50000 throws, Pi was estimated at:",estPi)
            return
        
    return throws
