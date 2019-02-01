#HOMEWORK ASSIGNMENT #3: "IF" STATEMENTS

def isEqual(a, b, c):
    if a == b or a == c:
        return True
    elif b == c:
        return True
    else:
        return False


#I have used different scenarios to show both true and False values


print(isEqual(1,1,2))#Where two are equal
print(isEqual(1,1,1))#Where two or more are equal
print(isEqual(1,2,2))#Again where two are equal 
print(isEqual(1,2,3))#Where none is equal
print(isEqual(4,5,6))#Where none is equal
print(isEqual(7,8,9))#Where none is equal




#For Extra Credits
def isEqual(a, b, c):
    if a or b or c is "":
        a = int(a)
        b = int(b)
        c = int(c)
        if a == b or a == c:
            return True
        elif b == c:
            return True
        else:
            return False
   
    
print(isEqual(6, 5, "5"))
print(isEqual(6, "6", 5))
print(isEqual(1, 2, 3))




"""For my own understanding"""


##def greater(a, b):
##    if a or b is "":
##        a = int(a)
##        b = int(b)
##        if a > b:
##            print("a is greater")
##        else:
##            print("b is greater")
##
##greater("6", 5)
