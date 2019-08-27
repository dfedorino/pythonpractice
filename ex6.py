"""
phrase = input("Your phrase:")
if len(phrase) < 1 : phrase = "Hello world"
print(phrase)
lst, lst_backwards = list(), list()
for i in phrase:
    if i == " " : continue
    lst.append(i.lower())
ind = len(lst) - 1 # 10 - 1
while ind >= 0:
    lst_backwards.append(lst[ind])
    ind -= 1
if lst == lst_backwards:
    print("Your phrase is a palindrome!")
else:
    print("Your phrase isn't a palindrome!")
"""
# the shortest solution:
inp = input("Your phrase:")
if inp.lower() == inp[::-1].lower() : print("{} is a palindrome.".format(inp))
else: print("{} is not a palindrome.".format(inp))
