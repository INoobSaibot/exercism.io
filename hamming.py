# 3.8.17 Hamming test attempt Tobias Stecker



'''
function
input 2 strings
compare strings
    indexNumbers 
count differenes per index
return count of differences
'''
firstString = ('AA')
secondString = ('BA')

def distance(firstString=None, secondString=None):
    #Declarations
    lengthFirstString =(len(firstString))
    lengthSecondString = (len(secondString))
    stringLength = (len(firstString))
    hammingDistance = 0
    #endDeclarations
    
    if lengthFirstString != lengthSecondString:
        raise ValueError
    for i in range (stringLength):
        #print(firstString[i] + " compare " + secondString[i])
        if firstString[i] != secondString[i]:
            hammingDistance += 1
    return hammingDistance

        





























