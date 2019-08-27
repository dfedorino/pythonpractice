# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or
# exactly right. (Hint: remember to use the user input lessons from the very
# first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends,
# print this out.
import random

def guessinggame():
    x = random.randint(1, 10)
    attempt = 0
    message = "Doesn't match! Your number is too {}. Try again."

    while True:
        try:
            num = int(input("Your number:\n"))
            if num not in range(1, 11) : print("Your number is out of range."); continue

            if num == x:
                attempt += 1
                return "You won! You had {} attempts.".format(attempt)
            else:
                if num in range(x, 11):
                    print(message.format("high")); attempt += 1
                else : print(message.format("low")); attempt += 1
        except:
            quit()

print(guessinggame())
