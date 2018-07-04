# CS5 Gold, hw2pr3
# Filename: hw2pr3.py
# Name: Will Wagner
# Problem description: Function Frenzy!

from math import *

#
# leng example from class
#
def leng(s):
    """leng returns the length of s  
        Yes, it's already built in as len(s), but...
        Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + leng(s[1:])

def flipside(s):
  """flipside swaps s's sides
     Argument s: a string
  """
  x = len(s)//2
  return s[x:] + s[:x]

#
# Tests
#
assert flipside('carpets')  == 'petscar'
assert flipside('homework') == 'workhome'
assert flipside('flipside') == 'sideflip'
assert flipside('az')       == 'za'
assert flipside('a')        == 'a'
assert flipside('')         == ''


#
# power example from class
#
def power(b, p):
    """power calculates b**p via recursion
       Argument: b, a number
       Argument: p, an integer
    """
    if p == 0:
        return 1
    elif p < 0:    # this is optional
        return 1.0/power(b, -p)
    else:
        return b*power(b, p - 1)


#
# add example--another, similar to the pow example above
#
def add(m, n):
    """add calculates m + n via recursion and adding 1
       Argument: m, a number
       Argument: n, an integer
    """
    if n == 0:
        return m
    else:
        return add(m, n - 1) + 1

################  Function 1
#
#     mult function
#
def mult(m, n):
    """ returns m * n using recursion
    """
    m1 = abs(m)
    #print("m1=",m1)

    if n == 0 or n==0:
        return 0

    if m<0 and n<0:
        return m1 + mult(m1, abs(n)-1)

    elif abs(m + n) != m + n:
        return (0-m1) - mult(abs(m), abs(n)-1)
    
    else:
        return m + mult(m, n-1)

#
# Mult Tests
#
assert mult(6, 7)   ==  42
assert mult(6, -7)  == -42
assert mult(-6, 7)  == -42
assert mult(-6, -7) ==  42
assert mult(6, 0)   ==   0
assert mult(0, 7)   ==   0
assert mult(0, 0)   ==   0

################  Function 2
# 
#  dot
# 

def dot(L, K):
    """ Returns the dot multiplier of two values submitted as lists
    """

    if leng(L) != leng(K):
        return 0.0

    elif L == [] or K == []:
        return 0.0

    else:        
        return ( L[0]*K[0] ) + dot( L[1:] , K[1:] )

#
# dot Tests
#
assert dot([5, 3], [6, 4])                       == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6])                          == 0.0
assert dot([], [6])                              == 0.0
assert dot([], [])                               == 0.0



################  Function 3
# 
#  ind
# 

def ind(e, L):
    """ Returns the index of a given string in a list
        If the item is not in the list it returns the number of items in the list
    """

    if e not in list(L):
        return leng(L[0:])

    for x in range( leng( list(L[0:]) ) ):    
        if e == L[x]:
            return x

#
# ind Tests
#
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100)))       == 42
assert ind('hi', ['hello', 42, True])     == 3
assert ind('hi', ['well', 'hi', 'there']) == 1
assert ind('i', 'team')                   == 4
assert ind(' ', 'outer exploration')      == 5



################  Function 4
#
#  Scrabble letterScore
#

def letterScore(let):
    """ Returns the Scrabble letter value for a given letter
    """

    if let in ("a","e","i","l","n","o","r","s","t","u"):    # 1 Score letters
        return 1

    elif let in ("d","g"):                    # 2 Score letters
        return 2

    elif let in ("b","c","m","p"):                  # 3 Score letters
        return 3

    elif let in ("f","h","v","w","y"):              # 4 Score letters
        return 4

    elif let in ("k"):                      # 5 Score letters
        return 5

    elif let in ("j","x"):                    # 8 Score letters
        return 8

    elif let in ("q","z"):                    # 10 Score letters
        return 10

    else:
        return 0

#
# Test every letter 
#

abc = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
for x in range(26):
    print(abc[x]," = ",letterScore(abc[x]))



################  Function 5
# 
#  scrabbleScore using For Loop
# 

def scrabbleScore(S):
    """ Returns the scrabble score for a given word
    """
    wordScore = 0

    if list(S) == "":
        return 0

    else:
        for x in range( leng( list(S[0:]) ) ):
            # print("Length of S:", leng( list(S[0:]) ), x, "letterScore: ", letterScore(S[x]) )
            wordScore +=letterScore(S[x]) 
            
    return wordScore

#
# Tests
#
assert scrabbleScore('quetzal')                    == 25
assert scrabbleScore('jonquil')                    == 23
assert scrabbleScore('syzygy')                     == 25
assert scrabbleScore('abcdefghijklmnopqrstuvwxyz') == 87
assert scrabbleScore('?!@#$%^&*()')                == 0
assert scrabbleScore('')                           == 0


################  Function 6
#
# DNA to RNA


def one_dna_to_rna(c):
        """Converts a single-character c from DNA
           nucleotide to complementary RNA nucleotide """
        if c == 'A':
            return 'U'
        elif c == 'C':
            return 'G'
        elif c == 'G':
            return 'C'
        elif c == 'T':
            return 'A'
        else:
            return ''

#
# vwl example from class
#
def vwl(s):
    """vwl returns the number of vowels in s
       Argument: s, which will be a string
    """
    if s == '':
        return 0   # no vowels in the empty string
    elif s[0] in 'aeiou':
        return 1 + vwl(s[1:])
    else:
        return 0 + vwl(s[1:])   # The 0 + isn't necessary but looks nice


def transcribe(S):
    """transcribe returns the RNA secuence from DNA
        it only accepts valid DNA in the form of ACGT
    """

    if S == '':
        return ''

    if S[0] not in 'ACGT':
        return "" + transcribe(S[1:])

    if S[1:] != "":
        # print(S[0], " = ", one_dna_to_rna(S[0]))
        # print( one_dna_to_rna(S[0]) + transcribe(S[1:]) )
        return one_dna_to_rna(S[0]) + transcribe(S[1:])

    else:
        return one_dna_to_rna(S[0])

#
# Tests
#
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU' # Note that the space disappears
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('cs5')      == ''        # Note that the other characters disappear
assert transcribe('')         == ''