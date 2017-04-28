#word count exercise by Tobias Stecker 3.8.17

testString = ("olly olly in come free")

'''
    make string list.split()
    make a copy of list
    get length of list
    compare each word[index] to each copywords[index]
        if they ==, and indexes not equal ad word to
            aWordsList2dArray or associative array/dictionary/hash
'''

def wordCount(sentenceString):
    listOfWords = (sentenceString.split())
    listOfWordsAsDictionary = {}
    occurancesOfCurrentWord = 0

    for each in listOfWords:
        occurancesOfCurrentWord = 0
        for eachCopy in listOfWords:
            if each == eachCopy:
                occurancesOfCurrentWord +=1
                occurances = str(occurancesOfCurrentWord)
        listOfWordsAsDictionary[each] = occurancesOfCurrentWord
    print(listOfWordsAsDictionary)    
    return
