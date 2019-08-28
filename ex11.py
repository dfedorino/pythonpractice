# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no
# divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

def prime(num):
    lst = [i for i in range(1, num) if i != 1 and num % i == 0]
    if sum(lst) > 0 : return "Your number is not prime."
    else : return "Your number is prime."

print(prime(int(input("Your number:\n"))))
