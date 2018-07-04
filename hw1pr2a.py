# coding: utf-8
# CS341
# Will Wagner
# hw1pr2a.py
#

import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
        answer n to end
    """

    valid_weapons = ['rock','paper','scissors']
    user = input("Choose your weapon: ")
    comp = random.choice(['rock','paper','scissors'])
    print()

    if user in valid_weapons:

        print('The user (you)   chose', user)
        print('The computer (I) chose', comp)
        print()

        if user == comp:
            print("Ha! We tied!  Great minds think alike!")

        elif user == 'rock' and comp != 'paper':
            congrats()

        elif user == 'paper' and comp != 'scisors':
            congrats()

        elif user == 'scisors' and comp != 'rock':
            congrats()

        else:
            print("Better luck next time...")

    else:
        print("That is not a valid weapon!  Please choose rock, paper, scissors.")


def congrats():
    """ function prints a random congratulations from the list grats 
    """

    grats = random.choice(["Well Done!","Good Stuff!","How'd you know I was gonna choose that?"])
    print("You Win! "+ grats) 


while True:
    rps()
    print()
    print("Still running...")
    print()
    response = input("Play again? Enter n to exit: ")
    if response == 'n':
        break
   
