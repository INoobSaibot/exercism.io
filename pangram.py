englishAlphabet = ('abcdefghijklmnopqrstuvwxyz')


#def is_pangram(sentence):
# define alphabet a to z
# define german_umlaute with accent marks
# convert case?
# looks for each letter from engllish alphabet in string, if not check german one
'''# for each in alphabet itterate sentence, does current letter each equal sentence iterative?
yes, sweet, else check for that letter against next iterative. if get to sentence end with out finding letter mark englilshMatch = false'''

# if english or german == True return True, else return False.
# return
    

test_sentence = '''Victor jagt zwölf Boxkämpfer quer über den'
                                   ' großen Sylter Deich.'''
test_sentence = "The quick brown fox jumps over the lazy dog."
#test_sentence ='juicey farts'

def go():
    is_pangram(test_sentence)





def is_pangram(sentence):
    #englishAlphabet = ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
    englishAlphabetKey =[]
    for each in englishAlphabet:
        englishAlphabetKey.append(each)
    foundLetters = []
    foundAlready = False
    pangram = None


    alphabet = englishAlphabet
    lowCaseSentence = sentence.lower()
    #lowCaseSentence = lowCaseSentence.split()
    for CurrentLetter in englishAlphabet:
        foundAlready = False
        for i in range(len(lowCaseSentence)):
            if foundAlready == False:
                sentenceChunk = lowCaseSentence[i]
                #print(sentenceChunk)
                #print (CurrentLetter)
                if CurrentLetter == sentenceChunk: # and foundAlready == False:
                    foundLetters.append(sentenceChunk)
                    foundAlready = True
    #print(foundLetters)
    if foundLetters == englishAlphabetKey:
        pangram = True
    else:
        pangram = False
    return (pangram)

