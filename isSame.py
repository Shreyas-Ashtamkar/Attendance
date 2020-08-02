def isSame(firstName:str, secondName:str):
    similarity = 0
    
    firstNameParts = firstName.split(' ')
    secondNameParts = secondName.split(' ')
    
    for partFirst in firstNameParts:
        for partSecond in secondNameParts:
            if partFirst.lower() == partSecond.lower():
                similarity += 1
    
    if similarity >2:
        similarity = 2
    
    returnValue = {
        0 : 'NO',
        1 : 'MAYBE',
        2 : 'YES'
    }
    
    return returnValue[similarity]