# Create a program that asks the user for a number and then prints out a list of
# all the divisors of that number. (If you don’t know what a divisor is, it is a
# number that divides evenly into another number. For example, 13 is a divisor of
# 26 because 26 / 13 has no remainder.)

# lst = []
# x = int(input("I'll show you all the divisors of your number. Give me the number, please:\n"))
# lst.append(x)
# y = x - 1
# while y != 0:
#    if x % y == 0:
#        lst.append(y)
#    y -= 1
# print(lst)

# IDEA:
x = int(input("I'll show you all the divisors of your number. Give me the number, please:\n"))
# lst = []
# for i in range(1, x + 1):
#    if x % i == 0:
#        lst.append(i)
# print(lst)
print([i for i in range(1, x + 1) if x % i == 0])
