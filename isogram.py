# Tobias Stecker Exercism.io
# is isogram exercise, 4.6.17
# updated 4.24.17

'''
    make string list.split to seperate letters
    compare each letter to each copyLetterList
    if letters ==, and indices not same add letter to
        return false,

    at bottom after all else, return true
    
'''

testWord = ("isograms")





def alphabetTest(singleLetter):
    #
    itsALetter = False
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    #
    
    for anAlphabetLetter in alphabet:
        if singleLetter == anAlphabetLetter:
            itsALetter = True
    
    return itsALetter

def is_isogram(theWord):
    """Takes string as the argument, returns trye if no letters are repeated"""
    #Declarations
    duplicateFound = False
    occurrences = 0
    #endDeclarations

    lettersInWord = list(theWord.lower())
    lettersInWordCopy = lettersInWord

    for outerLoopLetter in lettersInWord:
        if alphabetTest(outerLoopLetter) == True:
            #loopDeclarations
            occurrences = 0 #resets letter outer loop run, each letter will find itself once
            #endLoopDeclarations

            for innerLoopLetter in lettersInWord:
                if innerLoopLetter == outerLoopLetter:
                    occurrences += 1
                    
            if occurrences > 1: #eachletter should find itself once
                duplicateFound = True

    if duplicateFound == False: # duplicate not found inverts to isogram = True
        is_isogram = True
    else:
        is_isogram = False

    return is_isogram
            
            
                



















