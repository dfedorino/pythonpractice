# Make a two-player Rock-paper-Scissors game. (Hint: Ask for player plays
# (using input), compare them, print out a message of congratulations to the
# winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# paper beats rock
import random
#-------------------------------------------------------------------------------
# Module for singleplayer
#-------------------------------------------------------------------------------
def singleplayer():
    comp_count = 0
    p2_count = 0
    while True:
        el1, el2, el3 = 'paper', 'rock', 'scissors'
        combinations = {el1: el2, el2: el3, el3:el1}
        print("Count: {} : {}".format(comp_count, p2_count))
        try:
            comp = random.choice([el1, el2, el3])
            p2 = input("P2: {}/{}/{}?\n".format(el1, el2, el3))
            if comp.lower() not in [el1, el2, el3] or p2.lower() not in [el1, el2, el3]:
                message = input("Do you want to quit?y/n\n")
                if message == "y" : quit()
                continue
            if p2 == comp:
                print("\nFair!")
            elif p2 == combinations[comp]:
                print("\nAI wins!")
                comp_count += 1
                print("Count: {} : {}".format(comp_count, p2_count))
            else:
                print("\nP2 wins")
                p2_count += 1
                print("Count: {} : {}".format(comp_count, p2_count))
            message = input("Do you want to continue? y/n\n")
            if message == "y":
                print("-" * 10 + "Here you go!" + "-" * 10)
            else:
                quit()
        except:
            quit()
#-------------------------------------------------------------------------------
# Module for multiplayer
#-------------------------------------------------------------------------------
def multiplayer():
    p1_count = 0
    p2_count = 0
    while True:
        el1, el2, el3 = 'paper', 'rock', 'scissors'
        combinations = {el1: el2, el2: el3, el3:el1}
        print("Count: {} : {}".format(p1_count, p2_count))
        try:
            p1 = input("P1: {}/{}/{}?\n".format(el1, el2, el3))
            p2 = input("P2: {}/{}/{}?\n".format(el1, el2, el3))
            if p1.lower() not in [el1, el2, el3] or p2.lower() not in [el1, el2, el3]:
                message = input("Do you want to quit?y/n\n")
                if message == "y" : quit()
                continue
            if p2 == p1:
                print("\nFair!")
            elif p2 == combinations[p1]:
                print("\nP1 wins!")
                p1_count += 1
                print("Count: {} : {}".format(p1_count, p2_count))
            else:
                print("\nP2 wins")
                p2_count += 1
                print("Count: {} : {}".format(p1_count, p2_count))
            message = input("Do you want to continue? y/n\n")
            if message == "y":
                print("-" * 10 + "Here you go!" + "-" * 10)
            else:
                quit()
        except:
            quit()
choice = input("Singleplayer or Multiplayer? S/M")
if choice.lower() == "s":
    singleplayer()
elif choice.lower() == "m":
    multiplayer()
else:
    quit()
#-------------------------------------------------------------------------------
