"2nd attempt exercism.io ran transcription 2.21.17 a year later almost!"

testString = "ACGTGGTCTTAA"

def to_rna(inputString):
    #make is a list
    #for each in string testcase each dna code and return compliment dna codes
    #add those to outputList, make it a string, return string.

    # declarations
    rnaConversion = ''
    G_CONVERTED = 'C'
    C_CONVERTED = 'G'
    T_CONVERTED = 'A'
    A_CONVERTED = 'U'
    # endDeclarations
    
    for each in inputString:
        if each == "G":
            rnaConversion = rnaConversion + G_CONVERTED
        elif each == "C":
            rnaConversion = rnaConversion + C_CONVERTED
        elif each == "T":
            rnaConversion = rnaConversion + T_CONVERTED
        elif each == "A":
            rnaConversion = rnaConversion + A_CONVERTED
    return rnaConversion
    
