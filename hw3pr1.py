#
# hw3pr1.py
#
# Name: Will Wagner
#
# Turtle graphics and recursion
#

import time
from turtle import *
from random import *

def tri(n):
    """Draws n 100-pixel sides of an equilateral triangle.
       Note that n doesn't have to be 3 (!)
    """

    shape('turtle')
    if n == 0:
        return      # No sides to draw, so stop drawing
    else:
        width(2*n+1)
        forward(100)
        left(120)
        tri(n-1)    # Recur to draw the rest of the sides!

def spiral(initialLength, angle, multiplier):
    """Spiral-drawing function.  Arguments:
       initialLength = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    if initialLength <= 1:          
        return      # No more to draw, so stop this call to spiral
    else:
        forward(initialLength)
        left(angle)
        spiral(initialLength * multiplier, angle, multiplier)
        return

# spiral(100, 90, 0.9)
# spiral(100, 170, 0.95)
# spiral(2, 1, 0.999)

def chai(size):
    """Our chai function!"""
    if (size < 5): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2)
        right(90)

        chai(size/2)

        right(90)
        forward(size)
        left(90)

        chai(size/2)

        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return

# chai(100)

def svtree(trunklength, levels):
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
        # Draw the original trunk (1 line)
        forward(trunklength)

        # Turn a little bit to position the first subtree (1 line)
        left(50)

        # Recur! with both a smaller trunk and fewer levels (1 line)
        svtree(trunklength*.75, levels-1)
        
        # Turn the other way to position the second subtree (1 line)
        right(50)
        
        # Recur again! (1 line)
        svtree(trunklength*.75, levels-1)

        # Turn the other way to position the second subtree (1 line)
        right(50)

        # Recur again! (1 line)
        svtree(trunklength*.75, levels-1)
        
        # Turn and go BACKWARDS (2 steps: 2 lines)
        left(50)
        backward(trunklength)
        
        return

def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)



def flakeside(sidelength, levels):
    if levels == 0:
        forward(sidelength)
        return
        
    else:
        
        flakeside(sidelength,levels-1)

        right(60)
        flakeside(sidelength,levels-1)

        left(120)
        flakeside(sidelength,levels-1)

        right(60)
        flakeside(sidelength,levels-1)        

        return


