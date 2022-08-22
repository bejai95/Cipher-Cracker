# This program will decode a Substitution Cipher
# It uses some code/ideas from https://inventwithpython.com/hacking/chapter18.html

from wordPatternsGeneral import getWordPattern, createAllWordPatternsFile
from detectEnglish import getPercentageEnglishWords
import os, re, copy, itertools

# We want to import allWordPatterns, but the allWordPatterns.py file might not exist yet
if not os.path.exists('allWordPatterns.py'):
    createAllWordPatternsFile()
from allWordPatterns import allWordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersSpaceOrApostrophePattern = re.compile('[^A-Z\s\']')

def substitutionHackerPartial(cipherText):
    intersectedMapping = getIntersectedMapping(cipherText)
    key = getKeyBeforeFullDecipher(intersectedMapping)
    totalAmountPossibilities = getTotalAmountPossibilities(intersectedMapping)

    return {
        "totalAmountPossibilities": totalAmountPossibilities,
        "intersectedMapping": intersectedMapping,
        "plainText": decrypt(cipherText, key),
        "key": key
    }

def substitutionHackerFull(cipherText, intersectedMapping):
    newKey = fullDecipher(cipherText, intersectedMapping)

    return {
        "plainText": decrypt(cipherText, newKey),
        "key": newKey
    }

def getIntersectedMapping(cipherText):
    intersectedMapping = getBlankCipherletterMapping()
    
    # Remove characters that aren't letters, spaces and apostrophes from the ciphertext
    cipherTextEdited = nonLettersSpaceOrApostrophePattern.sub('', cipherText.upper())
    
    cipherWordList = cipherTextEdited.split()

    for cipherWord in cipherWordList:
        currentWordMapping = getBlankCipherletterMapping()
        currentWordPattern = getWordPattern(cipherWord)
        
        if currentWordPattern not in allWordPatterns:
            continue # The current word must not be in our dictionary, so continue

        # Add the letters of each candidate to the mapping
        for candidate in allWordPatterns[currentWordPattern]:
            addLettersToMapping(currentWordMapping, cipherWord, candidate)

        # Intersect the new mapping with the existing intersected mapping
        intersectedMapping = intersectMappings(intersectedMapping, currentWordMapping)
    
    # Remove any solved letters from the other lists.
    removeSolvedLettersFromMapping(intersectedMapping)

    # Convert Blanks => This needs to be done so that itertools.product can work it's magic
    convertBlanks(intersectedMapping)
    
    return intersectedMapping
        
def getBlankCipherletterMapping():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def addLettersToMapping(letterMapping, cipherWord, candidate):
    # Remember that in python, when dictionaries are passed as paramaters, what is passed is a copy of the dictionary reference value, instead of a copy of the dictionary value. This just means we can edit the dictionary directly. 

    for i in range(len(cipherWord)):
        if candidate[i] == "'": # Apostrophe
            continue
        elif candidate[i].upper() not in letterMapping[cipherWord[i]]:
            letterMapping[cipherWord[i]].append(candidate[i].upper())

    return

def intersectMappings(mapA, mapB):

    intersectedMapping = getBlankCipherletterMapping()
    
    for letter in LETTERS:
        
        # An empty list means "any letter is possible". In this case just copy the other map entirely
        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])
        
        else:
            # If a letter in mapA[letter] exists in mapB[letter], add that letter to intersectedMapping[letter]
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)
                    
    return intersectedMapping

def removeSolvedLettersFromMapping(letterMapping):
    loopAgain = True
    while loopAgain:
        loopAgain = False
        solvedLetters = []

        # If within the letterMapping there is only 1 letter corresponding to any cipherLetter, then add this letter to solvedLetters
        for cipherLetter in LETTERS:
            if len(letterMapping[cipherLetter]) == 1:
                solvedLetters.append(letterMapping[cipherLetter][0])

        # If there are any other cipherletter mappings that include a letter which has already been solved, remove it from those other cipherletter mappings
        for cipherLetter in LETTERS:
            for solvedLetter in solvedLetters:
                if len(letterMapping[cipherLetter]) != 1 and solvedLetter in letterMapping[cipherLetter]:
                    letterMapping[cipherLetter].remove(solvedLetter)

                    # If a new letter has now been solved, loop again
                    if len(letterMapping[cipherLetter]) == 1:
                        loopAgain = True
    
    return

def convertBlanks(letterMapping):
    for cipherLetter in LETTERS:
        if letterMapping[cipherLetter] == []:
            letterMapping[cipherLetter] = ["_"]
    
    return

def getKeyBeforeFullDecipher(intersectedMapping):
    keyBeforeFullDecipher = {}
    
    for cipherLetter in LETTERS:
        if len(intersectedMapping[cipherLetter]) > 1:
            keyBeforeFullDecipher[cipherLetter] = "_"
        else:
            keyBeforeFullDecipher[cipherLetter] = intersectedMapping[cipherLetter][0]
    
    return keyBeforeFullDecipher

def getTotalAmountPossibilities(intersectedMapping):
    totalAmountPossibilities = 1
    for key in intersectedMapping:
        amountOfPossibilitiesForKey = len(intersectedMapping[key])
        totalAmountPossibilities *= amountOfPossibilitiesForKey
    
    return totalAmountPossibilities

def fullDecipher(cipherText, intersectedMapping):
    
    cipherLetters = intersectedMapping.keys()
    values = (intersectedMapping[cipherLetter] for cipherLetter in cipherLetters)
    combinations = [dict(zip(cipherLetters, possibleKey)) for possibleKey in itertools.product(*values)]

    highestPercentageEnglish = 0
    bestKey = {}
        
    for combination in combinations:
        potentialKey = {}
        for cipherLetter in LETTERS:
            potentialKey[cipherLetter] = combination[cipherLetter][0]

        potentialPlainText = decrypt(cipherText, potentialKey)
        percentageEnglish = getPercentageEnglishWords(potentialPlainText)

        if percentageEnglish > highestPercentageEnglish:
            highestPercentageEnglish = percentageEnglish
            bestKey = potentialKey

    return bestKey

def decrypt(cipherText, key):
    
    plainText = []

    for character in cipherText:
        if character in LETTERS or character.upper() in LETTERS:
            if character in LETTERS:
                plainText.append(key[character])
            else:
                plainText.append(key[character.upper()].lower())
        else:
            plainText.append(character)
    
    plainText = ''.join(plainText)
    return plainText