# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd
# number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number
# to divide by (check). If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message.

num1 = int(input("""Hi, I'm here to give you some information about your number.
Firstly, give me your number, please:\n"""))
num2 = int(input("""Thank you, now give please the second number to divide by:
"""))

def odd_or_even(num1, num2):
    num1_remainder_4 = num1 % 4
    message1 = "Your first number is a multiple of 4 and is even. "
    num2_remainder_4 = num2 % 4
    message2 = "Your second number is a multiple of 4 and is even. "
    num1_remainder_2 = num1 % 2
    message3 = "Your first number is not a multiple of 4 but it is even. "
    num2_remainder_2 = num2 % 2
    message4 = "Your second number is not a multiple of 4 but it is even. "
    custom_remainder = num1 % num2
    message5 = "Your first number is odd. "
    message6 = "Your second number is odd. "
    num1_remainder_num2 = num1 % num2
    message7 = "Your first number is a multiple of the second number. "
    num2_remainder_num1 = num2 % num1
    message8 = "Your second number is a multiple of the first number. "
    message9 = "Your first number is not a multiple of the second number. "
    message10 = "Your second number is not a multiple of the first number. "
    # IDEA: You need to check both numbers first, then cocatenate the messages
    # Check of the 1st number:
    if num1_remainder_2 != 0:
        print(message5)
    if num1_remainder_2 == 0 and num1_remainder_4 != 0:
        print(message3)
    if num1_remainder_4 == 0:
        print(message1)
    # Check of the 2nd number:
    if num2_remainder_2 != 0:
        print(message6)
    if num2_remainder_2 == 0 and num2_remainder_4 != 0:
        print(message4)
    if num2_remainder_4 == 0:
        print(message2)
    # Check simultaneous division:
    if num1_remainder_num2 == 0:
        print(message7)
    else:
        print(message9)
    if num2_remainder_num1 == 0:
        print(message8)
    else:
        print(message10)

odd_or_even(num1, num2)
