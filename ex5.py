# Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that
# are common between the lists (without duplicates). Make sure your program
# works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at
# this point - we’ll get to it soon)

import random
lst1 = [random.randrange(10) for i in range(20)]
lst2 = [random.randrange(10) for i in range(10)]
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# lst2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst = []

# the shortest solution #1:
# for item in lst1:
#    if item in lst2:
#        if item not in lst:
#            lst.append(item)
# print (lst)

# the shortest solution #2:
# lst = list(set(lst1) & set(lst2))
#print(lst)

# My solution:
def count(lst):
    countlst = 0
    for i in lst:
        countlst += 1
    return countlst

def common_numbers(lst1, lst2):
    limit = count(lst1)
    ind = 0
    while ind < limit:
        item = lst1[ind]
        for i in lst2:
            if i == item:
                lst.append(i)
        ind += 1
    return lst

if count(lst1) <= count(lst2):
    print(common_numbers(lst1, lst2))
else:
    print(common_numbers(lst2, lst1))

def cut_copies(lst):
    limit = count(lst)
    ind = 0
    while ind < limit:
        for i in lst:
            if lst.count(i) > 1:
                a = lst.index(i)
                b = lst.pop(a)
            ind += 1
    return(lst)

print(cut_copies(lst))
