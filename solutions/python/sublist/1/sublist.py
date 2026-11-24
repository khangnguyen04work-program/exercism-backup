"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "Sublist"
SUPERLIST = "Superlist"
EQUAL = "Equal"
UNEQUAL = "Unequal"

def sublist(list_one, list_two):
    if list_one == list_two or (list_one == [] and list_two == []):
        return EQUAL
    if list_one == []:
        return SUBLIST
    if list_two == []:
        return SUPERLIST
    
    if len(list_one) < len(list_two):
        starting = 0
        ending = len(list_one)
        for i in range(len(list_two) - len(list_one) + 1):
            if list_two[starting:ending] == list_one: 
                return SUBLIST
            starting += 1
            ending += 1
            
    elif len(list_one) > len(list_two):
        starting = 0
        ending = len(list_two)
        for i in range(len(list_one) - len(list_two) + 1):
            if list_one[starting:ending] == list_two:
                return SUPERLIST
            starting += 1
            ending += 1
            
    return UNEQUAL

    