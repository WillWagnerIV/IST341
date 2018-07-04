# CS 5 Gold, hw3pr3
# filename: hw3pr3.py
# Name:
# problem description: List comprehensions



# this gives us functions like sin and cos...
from math import *



# two more functions (not in the math library above)

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2



# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [float(x//2) for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

# Here is where your functions start for the lab:

# Step 1, part 1
def unitfracs(N):
    """ Input: a number N
        Returns: a list of evenly-spaced left-hand endpoints (fractions) in the unit interval [0, 1].
    """
    return [x/N for x in range(N)]

assert unitfracs(2) == [0.0, 0.5]
assert unitfracs(5) == [0.0, 0.2, 0.4, 0.6, 0.8]
assert unitfracs(3) == [0.0, 0.3333333333333333, 0.6666666666666666]

# Step 1, part 2
def scaledfracs(low, hi, N):
    """ Input: Takes 3 numbers: low, hi, and an interval between them: N
        Returns:  creates N left endpoints uniformly through the interval [low, hi]
    """
    return [ y * (hi-low) + low for y in unitfracs(N) ]
    #return [ x * ((hi-low)/N) + low for x in range(N)]
    # return unitfracs(N) for x in unitfracs(N)  <--  experimental

assert scaledfracs(10, 30, 5) == [10.0, 14.0, 18.0, 22.0, 26.0]
assert scaledfracs(41, 43, 8) == [41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75]
assert scaledfracs(0, 10, 4) == [0.0, 2.5, 5.0, 7.5]

# Step 2, part 1
def sqfracs(low, hi, N):
    """ Input:  Takes 3 numbers: low, hi, and an interval between them: N
        Returns:  a list of the squares of evenly-spaced (fractions) in the unit interval [low, hi].
    """
    return [ ( x * ((hi-low)/N) + low ) ** 2 for x in range(N)]

assert sqfracs(4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert sqfracs(0, 10, 5) == [0.0, 4.0, 16.0, 36.0, 64.0]

# Step 2, part 2
def f_of_fracs(f, low, hi, N):
    """ Inout: f: a mathematical function ; Three variables specific to that function low, hi and an interval N.
        Returns: the results of the given function
    """
    return [ f( z ) for z in scaledfracs(low,hi,N)]

assert f_of_fracs(dbl, 10, 20, 5) == [20.0, 24.0, 28.0, 32.0, 36.0]
assert f_of_fracs(sq, 4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert f_of_fracs(sin, 0, pi, 4) == [0.0, 0.7071067811865475, 1.0, 0.7071067811865476]   # the sine function 

# Step 3
def integrate(f, low, hi, N):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where N steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of N uniform steps
       from low to hi
    """
    return ((hi-low)/N) * sum(f_of_fracs(f, low, hi, N))

assert integrate(dbl, 0, 10, 4) == 75
assert integrate(sq, 0, 10, 4) == 2.5 * sum([0, 2.5*2.5, 5*5, 7.5*7.5])

"""Q1
Question:
In a sentence explain why integrate will always underestimate the correct value of this particular integral.

Answer:
To correctly calculate the correct value, the interval N in the integration function would need to be infinitely large
to produce the requisite number of rectangles under the line.

Question:
As a follow up, what is a function whose integral would always be overestimated on the same interval, 
from 0 to 10? (If you're not sure about this, answer the next question first.)

Answer:
A line of increasing downward gradient would cause the integral to be overestimated, because the rectangles drawn
would extend outside the curve, rather than underneath it.
"""

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5


"""Q2
The function, c, traces a part of a circular arc with radius 2.

Out[1]: 3.732                    # rounded...
Out[2]: 3.228                    # rounded...
    
Q: Next, find the values of integrate(c, 0, 2, 200) and integrate(c, 0, 2, 2000) and make a note of them in your answer,
A: 3.1511769448395297, 3.1425795059119643 (see below)

Q: As N goes to infinity (i.e., becomes larger and larger), what does the value of this integral become? Why?
A: The value approaches Pi.

"""

# print(integrate(c, 0, 2, 2))
# 3.732050807568877
# print(integrate(c, 0, 2, 20))
# 3.2284648797549815
# print(integrate(c, 0, 2, 200))
# 3.1511769448395297                        <---------------
# print(integrate(c, 0, 2, 2000))
# 3.1425795059119643                        <---------------