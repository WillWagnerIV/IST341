#
# hw9pr4.py
# Will Wagner
# IST341 - Spring 2018
#
import math

def menu():
    """A function that simply prints the menu"""
    print()
    print("           Main Menu  ")
    print("           =========  ")
    print("(0) Input a new list in [n0,n1,n2] format")
    print("(1) Print the current list")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) Find the minimum and its day")
    print("(5) Find the maximum and its day")
    print("(6) Your TT investment plan")
    print("(7) Pan-Galactic Gargleblaster")
    print("(9) Break! (quit)")
    print()

def printList(L):
    """Prints the entire list L and the days"""
    print("{0: >3}   {1: >6}".format("Day", "Price"))
    print("{0: >3}   {1: >6}".format("---", "--------"))
    for x in list(range(len(L))):
        print("{0: ^3}   ${1: >6}".format((x+1), L[x]))
    return

def find_min_loc(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    minval = L[0]
    minloc = 0

    for i in list(range(len(L))):
        if L[i] < minval:  # a smaller one was found!
            minval = L[i]
            minloc = i

    return minval, minloc

def find_max_loc(L):
    """find max loc uses a loop to return the Maximumm price in L
            and the location (index or day) of that Maximum.
        Argument L: a nonempty list of numbers.
        Results:  the Largest value in L, its location (index)
    """
    maxval = L[0]
    maxloc = 0

    for i in list(range(len(L))):
        if L[i] > maxval:  # a bigger one was found!
            maxval = L[i]
            maxloc = i

    return maxval, maxloc

def find_best_buy(L):
    """find min loc uses a loop to return the minimum of L
            and the location (index or day) of that minimum.
        Argument L: a nonempty list of numbers.
        Results:  the smallest value in L, its location (index)
    """
    minval = L[0]
    minloc = 0

    for i in list(range(len(L)-1)):
        if L[i] < minval:  # a smaller one was found!
            minval = L[i]
            minloc = i

    return minval, minloc

def find_best_sell(L,minloc):
    """find max loc uses a loop to return the Maximumm price in L
            AFTER the min and the location (index or day) of that Maximum.
        Argument L: a nonempty list of numbers.
        Results:  the Largest value in L, its location (index)
    """
    maxval = 0
    maxloc = 0

    for i in list(range(len(L))):
        if i > minloc:
            if L[i] > maxval:  # a bigger one was found!
                maxval = L[i]
                maxloc = i

    return maxval, maxloc


def find_avg(L):
    """find avg uses a loop to return the avg of L.
       Argument L: a nonempty list of numbers.
       Return value: the average value of L.
    """
    total = 0
    cnt = 0
    for x in L:
        total += x
        cnt += 1
        avgPrice = total / cnt

    return avgPrice

def std_dev(L):
    """finds Standard Deviation of L.
       Argument L: a nonempty list of numbers.
       Return value: the Standard Deviation of L.
    """
    total = 0 
    L_av = find_avg(L)
    #print("L_av",L_av)
    for i in list(range(len(L))):
        total += (L[i] - L_av)**2
        #print("Total in loop",total)
    
    total = total / len(L)
    #print("total / len(L)",total)
    total = math.sqrt(total)
    #print("math.sqrt(total)",total)

    return total

def TT_inv_plan(L):
    # Find the best day to buy, then the best day after that to sell
    # minval, minloc = find_best_buy(L)
    # maxval, maxloc = find_best_sell(L,minloc)

    # Test list [5,5,5,10,50,2,49,1]

    minval = L[0]
    maxval = L[1]
    minloc = 0
    maxloc = 1
    new_dif = 0
    old_dif = 0

    # Use nested loop to check each value in the list L
    for i in list(range(len(L))):
        for nested_i in list(range(i,len(L))):
            new_dif = L[nested_i] - L[i]
            if (new_dif) > old_dif:
                old_dif = new_dif
                minval = L[i]
                minloc = i
                maxval = L[nested_i]
                maxloc = nested_i

    print()
    print("TT Investments recommends that you will have done the following:")
    print("Buy on Day",minloc+1,"at $",minval)
    print("Sell on Day",maxloc+1,"at $",maxval)
    print("Profit per share: $",maxval-minval)

    return

def main():
    """The main user-interaction loop"""

    L = [30, 10, 20]  # an initial list

    while True:     # the user-interaction loop
        # print("\n\nThe list is", L)
        # print("\n\n")
        menu()
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
        if choice == 9:    # We want to quit
            break          # Leaves the while loop altogether

        elif choice == 0:  # We want to enter a new list
            newL = input("Enter a new list: ")    # enter _something_
            
            #
            # "Clean and check" the user's input
            #
            try: 
                newL = eval(newL)   # eval runs Python's interpreter! Note: Danger!
                if type(newL) != type([]): 
                    print("That didn't seem like a list. Not changing L.")
                else: 
                    L = newL  # Here, things were OK, so let's set our list, L
            except:
                print("I didn't understand your input. Not changing L.")

        elif choice == 1:  # Print the current list
            printList(L)

        elif choice == 2:  # Find the Average Price
            avgPrice = find_avg(L)
            print("\n\nThe average Price is", avgPrice)

        elif choice == 3:  # Find the Standard Deviation
            stdDev = std_dev(L)
            print("\n\nThe Standard Deviation is", stdDev)

        elif choice == 4:  # Find the Min Val and Day
            minval, minloc = find_min_loc(L)
            print("\n\nThe Minimum Price is", minval, "at day #", minloc+1)

        elif choice == 5:  # Find the Max Val and Day
            maxval, maxloc = find_max_loc(L)
            print("\n\nThe Maximum Price is", maxval, "at day #", maxloc+1)

        elif choice == 6:  # TT Investment Plan
            TT_inv_plan(L)

        elif choice == 7:  # Pan-Galactic Gargleblaster
            
            print("In order to smooth the highs and lows of the stock market,")
            print("You may be driven to extreme drinking which might include")
            print("a desire for a Pan-Galactic Gargleblaster.")
            print("Since they are unavailable on this planet,")
            print("here are are the steps to recreate the sensation")
            print("(According to the Guide).")
            print()
            print("How to simulate a Pan-Galactic Gargleblaster:")
            print("Step 1: Cook Pasta")
            print("Step 2: Wrap pasta around gold brick.")
            print("Step 3: Hit yourself in head with aforementioned gold brick.")
            print()
            print("If you're still thirsty, repeat as necessary.")

        else:
            print(choice, " ?      That's not on the menu!")

    print()
    print("So long and thanks for all the fish!")