#
# hw6pr5.py - Intro to loops!
#
# Name:
#

def fac(n):
    """ loop-based factorial function 
        input: a nonnegative integer n
        output: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# tests for looping factorial
#

print("fac(0): should be 1 ==", fac(0))
print("fac(5): should be 120 ==", fac(5))

#
# Looping function to write #1
# 

def power(b,p):
    """

    """
    result = 1                 # starting value - like a base case
    for x in range(1,p+1):     # loop from 1 to p, inclusive
        result = result * b    # update the result by mult. by b
    return result

print("power(2,5): should be 32 ==", power(2,5))
print("power(5,2): should be 25 ==", power(5,2))
print("power(42,0): should be 1 ==", power(42,0))
print("power(0,42): should be 0 ==", power(0,42))
print("power(0,0): should be 1 ==", power(0,0))


#
# Looping function to write #2
# 

def summed( L ):
    """ loop-based function to return a numeric list, summed
        (sum is built-in, so we're using a different name)
        input: L, a list of integers
        output: the sum of the list L
    """
    result = 0
    for e in L:
        result = result + e    # or result += e
    return result

# tests!
print("summed( [4,5,6] ): should be 15 ==", summed( [4,5,6] ))
print("summed( range(3,10) ): should be 42 ==", summed( range(3,10) ))

def summedOdds(L):
    """ loop-based function to return a numeric list, with only the odd elements summed
        (sum is built-in, so we're using a different name)
        input: L, a list of integers
        output: the sum of the list L
    """
    result = 0
    for e in L:
        if e % 2 == 1:             # use Mod to find odds
            result = result + e    # or result += e
        else:
            result = result + 0    # 0 isn't required but looks good
    return result

print("summedOdds( [4,5,6] ): should be 5 ==", summedOdds( [4,5,6] ))
print("summedOdds( range(3,10) ): should be 24 ==", summedOdds( list(range(3,10)) ))

#
# Looping function to write #3: untilARepeat( high )
# Sample functions
#

import random

def countGuesses( hidden ):
    """ uses a while loop to guess hidden, from 0 to 99
        input: hidden, a "hidden" integer from 0 to 99
        output: the number of guesses needed to guess hidden
    """
    guess = random.choice( range(0,100) )       # 0 to 99, inclusive 
    numguesses = 1                              # we just made one guess, above
    while guess != hidden:
        guess = random.choice( range(0,100) )   # guess again!
        numguesses += 1                         # add one to our number of guesses
    return numguesses


def unique( L ):
  """ returns whether all elements in L are unique
      input: L, a list of any elements
      output: True, if all elements in L are unique,
           or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique( L[1:] )  # recursion is OK, too!

#
# untilARepeat
# Assignment function
#

def untilARepeat( high ):               # Takes a number of iterations
    """ Input: A number (high) of tries to test if a random number repeats in a list
        Returns the number of tries before a random number is repeated
    """
    L = [ ]                             # Running list of numbers already checked
    #guess = [ ]                      # Storage to convert guess to list
    numTries = 0                        # Number of tries

    while unique ( L ) == True:
        guess = random.choice( range(0,high+1) )
        #print(guess)                    # Only used for debugging
        L = L + [guess]
        numTries += 1
        #print(L)                        # Only used for debugging

    return numTries

print("10000 iterations of untilARepeat:")
print("This takes a little time...")
L = [ untilARepeat( 365 ) for i in range(10000) ]
 
print("Sum = ", sum(L)/10000.0) 
print("Max = ", max(L))  
print("Min = ", min(L))
print("42 in L =", 42 in L)                
