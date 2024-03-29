# Take two lists, say for example these two:
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that
# are common between the lists (without duplicates). Make sure your program
# works on two lists of different sizes. Write this using at least one list
# comprehension. (Hint: Remember list comprehensions from Exercise 7).

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
bUnique = list()
for i in b:
    if i not in bUnique:
        bUnique.append(i)
print([i for i in bUnique if i in a])
