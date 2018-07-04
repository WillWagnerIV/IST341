# coding: utf-8
#
# hw1pr2b.py
#

# 
#   Done - An if, elif, and else control structure (with exactly one elif)
#   Done - An if, elif, elif, ... and else control structure (with at least two elifs)
#   Done - An if, else control structure (with zero elifs)
#   Done - An if, elif, ... control structure (with one or more elifs but no trailing else at all)
#   Done - An if control structure (with no trailing elif nor trailing else at all) 


""" 
Title for your adventure:   The Quest.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.

"""

import time


def table_adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
    """
    delay = 0.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    username = input("What do they call you, worthy adventurer? ")

    print()
    print("Welcome,", username, " to the Libra Complex, a labyrinth")
    print("of weighty wonders and unreal quantities...of poptarts and cereal!")
    print()

    print("Your quest: To find--and partake of--a poptart and make a bowl of cereal!")
    print()
    flavor = input("What flavor do you seek? ")
    if flavor == "strawberry":
        print()
        print("Wise! You show deep poptart experience.")
    elif flavor == "s'mores":
        print()
        print("The taste of the campfire: well chosen, adventurer!")
    else:
        print()
        print("Each to their own, then.")
    print()

    print("On to the quest!\n\n")
    print("A corridor stretches before you; its dim lighting betrays, to one side,")
    print("a table supporting nameless forms of inorganic bulk and, to the other,")
    print("a door ajar, leaking laughter--is that laughter?--of lab-goers.")
    time.sleep(delay)
    print()

    choice1 = input("Do you choose the table or the door? [table/door] ")
    print()

    if choice1 == "table":
        print()
        print("As you approach the table, its hazy burdens loom ever larger, until...")
        time.sleep(delay)
        print("...they resolve into unending stacks of poptarts, foil shimmering.")
        print("You succeed, sumptuously, in acquiring the poptarts.")
        
        print()
        print("Now,", username, " two ovens emerge from the mist!")
        print("Will you choose the crispy goodness of the toaster, ")
        print("the lightning-quick satisfaction of the microwave, ")
        print("or perhaps you'll prefer the instant gratification of an uncooked poptart?")
        print()
        choice2 = input("[toaster/microwave/uncooked]")
        print()

        if choice2 != "toaster":
            print()
            print("I prefer the traditional taste of a toaster, but to each their own.")


    else: 
        print() 
        print("You push the door into a gathering of sagefowl, athenas, and stags alike,")
        print("all relishing their tasks. Teamwork and merriment abound here, except...")
        time.sleep(delay)
        print("...they have consumed ALL of the poptarts! Drifts of wrappers coat the floor.")
        print("Dizzy, you grasp for a pastry. None is at hand. You exhale and slip")
        print("under the teeming tide of foil as it finishes winding around you.")
        print("Farewell,", username, ".")


def cereal_adventure():

    print("Having acquired your breakfast repast you are ready to start your day.")
    print("As you proceed towards the light of the glorious day that awaits you,")
    print("the infamous Breakfast Gnome darts from the shadows and challenges you with a question:")
    cereal_choice = input("What is the proper order to put cereal and milk in the bowl? [cereal then milk] Hint: add sugar")
   

    if cereal_choice == "cereal then milk then sugar":
        print()
        print("Sweet tooth in the morning, hunh?")

    elif cereal_choice == "milk then cereal":
        print()
        print("The Gnome laughs and says,'Clearly a breakfast novice")

    elif cereal_choice == "cereal then milk":
        print()
        print("Minimal cereal - acceptable but not awesome.")

    elif cereal_choice == "cereal then milk then sugar":
        print()
        print("If you put the sugar in first it mixes with the milk - rookie!")

    elif cereal_choice == "cereal then milk then strawberries":
        print()
        print("Nice!  Enjoy a hearty bowl of breakfast lovin'!")

    else:
        print()
        print("The Breakfast Gnome doesn't seem to understand")
        

table_adventure()
cereal_adventure()


again = input("I'm sure you're gonna have a great day.  Would you like to play agian? [y/n]")
print()
if again == "y":
    table_adventure()
    cereal_adventure()
    print()
    print("You know how to beak your fast! You're gonna have a great day!")

elif again == "n":
    print()
    print("You know how to break your fast! You're gonna have a great day!")
