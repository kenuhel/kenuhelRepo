def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total


def blanckSpaces(arg):
    countB = 0
    for count in arg:
        if count == " ":
            countB +=1
    return countB

def isAnEmail(arg):
    email = False
    for p in arg:
        if p == "@":
            email = True
    return email
    



