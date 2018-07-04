#
# hw9py5.py
# Will Wagner
# IST341 - Spring 2018

import time

print("Please try the function 'UltraCrazyStripedDiamond()'")
def printRect (width,height,symbol):
    """ Prints a rectangle width x height using symbol
    """
    for y in range(height):
        for x in range(width):
            print(symbol, end=" ")
        print(end='\n')

def printTriangle (width,symbol,rightSideUp):
    """ Prints a rectangle width x height using symbol
    """
    if rightSideUp:
        cnt=1
    else:
        cnt=width
        
    for y in range(1, width+1):
            for x in range(cnt):
                print(symbol, end=" ")
            print(end='\n')
            if rightSideUp:
                cnt += 1
            else:
                cnt -= 1

def printBumps(num, symbol1, symbol2):
    """ Prints bumps along the left margin equal to the height
        and number of nums using symbol1 for the top half
        and symbol2 for the bottom half of each bump.
    """
    for bump in range(1, num+1):
        for bump_row in range(1, bump+1):
            # Top Half
            for topHalf in range(1,bump_row+1):
                print(symbol1,end=" ")
            print(end='\n')
        # Bottom Half
        while bump_row > 0:
            cnt = bump_row
            while cnt > 0:
                print(symbol2,end=" ")
                cnt -= 1
            print(end='\n')
            bump_row -= 1


def printDiamond(width, symbol):
    """ Prints a diamond of symbol whose maximum width
        is determined by width. 
    """
    for row in range(1, width+1):

        print(" " * (width-(row-1)),end=" ")
        for s in range(row):
            print(symbol, end = " ")
        print(end='\n')
        row -= 1

    while row > 0:

        print(" " * (width-(row-1)),end=" ")
        for s in range(row):
            print(symbol, end = " ")
        print(end='\n')
        row -= 1


def printStripedDiamond (width, symbol1, symbol2):
    """ Prints a striped diamond of width, alternating between
        symbol1 and symbol2
    """

    for row in range(1, width+1):
        
        symbol = symbol1
        print(" " * (width-(row-1)),end=" ")
        for s in range(row):
            print(symbol, end = " ")
            if symbol == symbol1:
                symbol = symbol2
            else:
                symbol = symbol1
        print(end='\n')
        row -= 1

    while row > 0:

        print(" " * (width-(row-1)),end=" ")

        if row % 2 == 1:
            symbol = symbol1
        for s in range(row):
            print(symbol, end = " ")
            if symbol == symbol1:
                symbol = symbol2
            else:
                symbol = symbol1
        print(end='\n')
        row -= 1


def printCrazyStripedDiamond(width, symbol1, symbol2, sym1Width, sym2Width):
    """ prints a "striped diamond" of sym1 and sym2 
        where the stripes can have varied widths. 
        sym1Width determines the width of the stripe made of symbol 1 
        sym2Width determines the width of the stripe made of symbol 2
    """
    
    #
    # create the middle row using loops
    # 

    middle_row = ""
    symbol = symbol1
    sym_width = sym1Width
    sym_ctr = 0
    char_counter = 0

    while char_counter < width :
        for stripes in range(2):
            while sym_ctr < sym_width:
                if char_counter < width:
                    middle_row = middle_row + symbol + " "
                sym_ctr += 1
                char_counter += 1

            #print(stripes,middle_row)
            sym_ctr = 0
            if symbol == symbol1:
                symbol = symbol2
                sym_width = sym2Width
            else:
                symbol = symbol1
                sym_width = sym1Width

    

    #
    # Create the diamond
    #

    # Top Half

    row = 1

    while row <= width:
    
        print(" " * (width-row),end=" ")    # print the blank spaces

        print(middle_row[0 : row*2])

        row += 1

    # Bottom half
    row -= 1
    bottom_row = middle_row[1:]

    while row >= 0:

        print(" " * (width-row),end=" ")    # print the blank spaces

        print(bottom_row)
        
        row -= 1
        bottom_row = bottom_row[2:]
        

def UltraCrazyStripedDiamond():
    """ This function draws a diamond.
        The function prompts the user for the width of the diamond,
        then it promts the user for the number of stripes,
        then prompts for each width, character and color.
        The color must be R for Red, G for Green or B for Blue.
    """
    while True:     # the user-interaction loop
        UltraMenu()
        choice = input("Choose an option: ")
        #
        # "Clean and check" the user's input
        # 
        try:
            choice = int(choice)   # make into an int!
        except:
            print("I didn't understand your input! Continuing...")
            continue

        # run the appropriate menu option
        #
        if choice == 0:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 1:  # We want to create a new diamond
            createDiamond()

        elif choice == 2:  # Edit the Diamond
            pass

        



def UltraMenu():
    """ Creates the menu for the UltraCrazyStripedDiamond """

    print()
    print("           Ultra-Crazy Diamond Maker ")
    print("           =========================  ")
    print("(0) Quit")
    print("(1) Create a Diamond")
    print("(2) Edit Current Diamond (Not Implemented Yet)")

    print()

def createDiamond():
    """ Get the user's input for the diamond.  
        The function prompts the user for the width of the diamond,
        then it promts the user for the number of stripes,
        then prompts for each width, character and color.
        The color must be R for Red, G for Green or B for Blue.
    """

    stripe_width = []
    stripe_char = []
    stripe_color = []

    colors =   {"e": "\033[0m",
                "r": "\033[91m",
                "g":'\033[92m',
                "b":'\033[94m'}

    # print(colors['r'] + 'Success!' + '\x1b[0m')

    width = input("Enter a width for the Diamond:")
    try:
        width = int(width)   # make into an int!
    except:
        print("I didn't understand your input! Continuing...")
    num_stripes = input("Enter the number of stripes:")
    try:
        num_stripes = int(num_stripes)   # make into an int!
    except:
        print("I didn't understand your input! Continuing...")
    for x in range(num_stripes):
        print("Enter a width for Stripe",x+1,":",end=" ")
        stripe_width += input()
        try:
            stripe_width[x] = int(stripe_width[x])   # make into an int!
        except:
            print("I didn't understand your input! Continuing...")
        print("Enter the character for Stripe",x+1,end=" ")
        stripe_char += input()
                
        print("Choose r, g or b for Stripe",x+1,end=" ")
        stripe_color += input()
       
        # print(colors[stripe_color[x]]+ 'TEST OF COLOR' + colors['e'])

    # Print the diamond

    #
    # create the middle row using loops
    # 

    middle_row = ""
    sym_color = stripe_color[0]
    sym_ctr = 0
    char_counter = 0

    while char_counter < int(width) :  # whole string
        for stripes in range(num_stripes):
            while sym_ctr < stripe_width[stripes]:
                #print("Stripe width of ",stripes,":",stripe_width[stripes])
                if char_counter < width:
                    middle_row += stripe_char[stripes] + " "                
                char_counter += 1
                sym_ctr += 1
            #print(stripes,middle_row)
            sym_ctr = 0

    #
    # Print the diamond
    #

    # Top Half
    print()
    print()

    row = 1

    while row <= width:
    
        print(" " * (width-row),end=" ")    # print the blank spaces

        print(middle_row[0 : row*2])

        row += 1

    # Bottom half
    row -= 1
    bottom_row = middle_row[1:]

    while row >= 0:

        print(" " * (width-row),end=" ")    # print the blank spaces

        print(bottom_row)
        
        row -= 1
        bottom_row = bottom_row[2:]
        
    return





''' Check this out! '''
#              !!!!!!    !!!!!!!!    !!!!!!
# I was investigating adding colors to the stripes and I found
#   this handy nested loop!

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

    

    

