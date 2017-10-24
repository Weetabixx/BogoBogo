# imports
from random import shuffle


"""
Bogobogosort specifies how one should check if the list of numbers is sorted.
It does it recursively, because as anyone who knows anything at all about computer science knows,
recursion is always good and cool. To check if the list is sorted, use the following procedure:
1. Make a copy of the list of numbers.
2. Sort the first n-1 elements of the copy using bogobogosort.
3. Check to see if the nth element of the sorted copy is greater than the highest element of the first n-1 elements.
    If so, the copy is now sorted, else randomise the order of the elements of the copy and go to step 2.
4. Check to see if the copy is in the same order as the original list.

-courtesy of u/Kingmudsy from reddit
"""
m = int(input("how large would you like the list?/n"))
x = [i for i in range(m)]  # create list
shuffle(x)  # mix list
print("list: " + str(x))
totalComps = 0

def bogobogo(listToSort):
    n = len(listToSort)
    if n < 2:
        return listToSort  # a list of size 1 is already ordered
    ordered = False
    copyOfList = list(listToSort)  # create copy of list
    while ordered == False:
        bogoSortedCopy = bogobogo(copyOfList[:-1])  # sort n-1 first elements of copy using bogobogo sort
        ordered = (bogoSortedCopy[-1] <= copyOfList[-1])  # compare last element of sorted n-1 list and listToSorts last
        global totalComps  # count how many times a comparison is done
        totalComps += 1
        if ordered:  # if copy is sorted then return ordered list
            orderedList = list(bogoSortedCopy + [copyOfList[-1]])
            return orderedList
        else:  # if not sorted then shuffle copy and bogobogo sort the copy n-1 first elements again
            shuffle(copyOfList)


clear = bogobogo(x)
print("ordered the list yay!")
print(str(clear))
print("took " + str(totalComps) + " comparisons")
