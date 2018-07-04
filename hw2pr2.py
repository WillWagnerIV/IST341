
# CS5 Gold, Lab2 part 2
# Filename: hw2pr2.py
# Name: 
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

def sq(x):
    """Return value of x squared
       Argument x: a number (int or float)
    """
    return x*x

def interp(low, hi, fraction):
    """ Return value that is fraction of the distance between low and hi
    """

    return ((hi-low)*fraction)+low

def checkends(s):
    """Returns true if the first and last characters are the same
    """

    if s[0] == s[-1]:
        return True
    else:
        return False

def flipside(s):
    """Returns a string with the second half of an inputted string moved to the front
    """

    x = len(s)//2    # finds midpoint of the string as an integer

    firsth = s[0:x]
    secondh = s[x:]

    return secondh + firsth

def convertFromSeconds(s):
    """Converts an number of seconds in to days, hours, minutes and seconds
    """

    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60 * 60)
    s = s % (60*60)
    minutes = s // 60
    seconds = s % 60
    return [days, hours, minutes, seconds]

# print(convertFromSeconds(100000))
