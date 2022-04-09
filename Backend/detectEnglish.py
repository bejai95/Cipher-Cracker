# This program detects whether a given string is English based on the percentage of its words which are in the English dictionary
# It uses some code from https://inventwithpython.com/hacking/chapter12.html

THRESHOLD_PERCENTAGE = 60
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n\''

def getAllEnglishWords(): 
    dictionaryFile = open('dictionary.txt', "r")
    AllEnglishWords = {}
    
    for word in dictionaryFile.read().split('\n'):
        AllEnglishWords[word.lower()] = None
    
    dictionaryFile.close()
    return AllEnglishWords

ALL_ENGLISH_WORDS = getAllEnglishWords()

def removeNonLettersAndSpace(string):
    ret = []
    for character in string:
        if character in LETTERS_AND_SPACE:
            ret.append(character)
    return ''.join(ret)

def getPercentageEnglishWords(string):
    adjustedString = removeNonLettersAndSpace(string.lower())
    possibleWords = adjustedString.split()

    matches = 0
    for word in possibleWords:
        if word in ALL_ENGLISH_WORDS:
            matches += 1

    return (matches / len(possibleWords)) * 100

def isEnglish(string):
    percentageEnglishWords = getPercentageEnglishWords(string)
    return percentageEnglishWords >= THRESHOLD_PERCENTAGE