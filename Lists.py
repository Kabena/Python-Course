#HOMEWORK ASSIGNMENT #4: LISTS

"""
In this assignment, I am going to create a global variable for a list.
Thereafter, I shall create a function that allows anything to be added to
the list. However, if whatever is being added to the list already exists
in the list, the function should not add it to the list
rather discard it and return "False"
Otherwise, the value is added to the list and the function returns a "True".
"""

#create a global variable
myUniqueList = []

#create a function to add values to the list
def addToList(value):
    if value in myUniqueList:
        return False
    else:
        myUniqueList.append(value)
        return True

print(addToList(1))
print(addToList(2))
print(addToList(3))
print(addToList(4))
print(addToList(5))
print(addToList(1))
print(addToList(2))
print(addToList(6))
print(myUniqueList)



#For Extra Credit
#Another global variable
myLeftOvers = []
mySecondList = []

#function to add values to the list and put all rejected values to new list

print('\n')
print("This is the second part of the assignment")
def addToList2(value):
    if value in mySecondList:
        myLeftOvers.append(value)
        return False
    else:
        mySecondList.append(value)
        return True

print(addToList2(1))
print(addToList2(2))
print(addToList2(3))
print(addToList2(4))
print(addToList2(5))
print(addToList2(1))
print(addToList2(2))
print(addToList2(3))
print(addToList2(4))
print(addToList2(5))
print(addToList2(6))
print(addToList2(7))
print(mySecondList)
print(myLeftOvers)
