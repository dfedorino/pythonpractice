# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will
# turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and
# printing out that many copies of the previous message. (Hint: order of
# operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint:
# the string "\n is the same as pressing the ENTER button)

#---------------------------------------------------------------------------------------------------------------------------------------
# 2019-07-31 - my first solution
print("""It's time to know the year when you will turn 100 years old. Here are
several questions for me to know about you:""")
name = input("Your name:\n")
age = input("Your age:\n")
current_year = 2019
anniversary = 100 - int(age) + current_year
final_message = ("Okay, " + name + ", you will turn 100 years old in:\n" +
str(anniversary) + "\n")
print(final_message)
print("Now let's play a bit. Give me a number:")
times = input(">")
print("Surprise!")
print(final_message * int(times))
#---------------------------------------------------------------------------------------------------------------------------------------
# Another solution:
# import datetime
# now = datetime.datetime.now()

# name = input("Hey, what's your name?\n")
# age = int(input("Okay {}, how old are you?\n".format(name.title())))
# yrs = (now.year +100) - age
# msg = "Okay {}, so if you're {} now then you should turn 100 in the year {}".format(name.title(),age,yrs)
# print(msg)
# n = int(input("Okay {}, give me a number\n".format(name)))

# print(msg * n)
# print("Or does this look nicer?")
# msg += "\n"
# print(msg * n)
#---------------------------------------------------------------------------------------------------------------------------------------
# 2019-08-27 - my refactored solution
# import datetime
# now = datetime.datetime.now()

# m = "Okay, {}, you will turn 100 years old in {}\n".format(input("""Hi, user!
# I'll tell you the year you'll turn 100 y.o. Your name:\n"""),
# (now.year + 100) - int(input("Your age:\n")))
# print(m)
# print(m * int(input("Now let's play a bit. Give me a number:\n>")))
