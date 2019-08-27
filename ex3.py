# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less
# than 5.

# Extras:
# Instead of printing the elements one by one, make a new list that has all the
# elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from
# the original list a that are smaller than that number given by the user.

lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst2 = []
inp = input("Number to compare:\n")
try:
    num = int(inp)
except:
    check = input("Invalid input.\n Do you want to try one more time?Y/N\n")
    if check == "Y":
        inp = input("Number to compare:\n")
        num = int(inp)
def compare(lst1, lst2, num):
    for i in lst1:
        if i < num:
            lst2.append(i)
    print(lst2)

compare(lst1, lst2, num)
