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

def substitutionHacker(cipherText):
    intersectedMapping = getIntersectedMapping(cipherText)
    print(intersectedMapping)
    

    cipherLetters = intersectedMapping.keys()
    values = (intersectedMapping[cipherLetter] for cipherLetter in cipherLetters)
    possibleKeys = [dict(zip(cipherLetters, possibleKey)) for possibleKey in itertools.product(*values)]

    highestPercentageEnglish = 0
    bestKey = {}
    
    for potentialKey in possibleKeys:
        potentialKeyTranslated = {}
        for cipherLetter in LETTERS:
            potentialKeyTranslated[cipherLetter] = potentialKey[cipherLetter][0]

        potentialPlainText = decrypt(cipherText, potentialKeyTranslated)
        percentageEnglish = getPercentageEnglishWords(potentialPlainText)

        if percentageEnglish > highestPercentageEnglish:
            highestPercentageEnglish = percentageEnglish
            bestKey = potentialKeyTranslated
    
    return {
        "plainText": decrypt(cipherText, bestKey),
        "key": potentialKeyTranslated
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

    # Convert Blanks
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
    #listOfRemainingLetters = list(LETTERS)
    #for cipherLetter in LETTERS:
    #    if len(letterMapping[cipherLetter]) == 1:
    #        listOfRemainingLetters.remove(letterMapping[cipherLetter][0])
    
    
    for cipherLetter in LETTERS:
        if letterMapping[cipherLetter] == []:
            letterMapping[cipherLetter] = ["_"]
    
    return


def decrypt(cipherText, key):
    # Decrypt the cipherText using the key
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






def main():
    data = substitutionHacker("""Tvs ythsl bvs npstbwrq sgsq bvrpjv tvs lwlq'b usykkm fyqb br vsyu bvs yqtfsu. Wb fyt y qr-fwq twbpybwrq twqes tvs ykusylm hqsf. Wi vs brkl bvs bupbv, tvs'l jsb erqiwuoybwrq ri vsu frutb isyut. Wi vs kwsl, tvs'l hqrf bvyb vs fytq'b fvr tvs bvrpjvb vs fyt fvwev frpkl cs ykortb yt cyl. Msb tvs ythsl bvs npstbwrq yqmfym yql fywbsl iru vwt yqtfsu.

Trosbwost wb't bvs iwutb orosqb ri bvs lym bvyb eybevst mrp rii jpyul. Bvyb't fvyb Fsqlm fyt bvwqhwqj. Tvs rxsqsl vsu fwqlrf br tss iwus sqjwqst teussevwqj lrfq bvs tbussb. Fvwks bvwt fytq'b trosbvwqj eroxksbskm pqvsyul ri, wb yktr fytq'b qruoyk. Wb fyt y tpus twjq ri fvyb fyt jrwqj br vyxxsq bvyb lym. Tvs erpkl issk wb wq vsu crqst yql wb fytq'b bvs fym tvs fyqbsl bvs lym br csjwq.

Xybuweh lwlq'b fyqb br jr. Bvs iyeb bvyb tvs fyt wqtwtbwqj bvsm optb jr oyls vwo fyqb br jr sgsq kstt. Vs vyl qr lstwus br oyhs toykk bykh fwbv tbuyqjsut vs frpkl qsgsu yjywq tss dptb br cs xrkwbs. Cpb tvs wqtwtbsl bvyb Xybuweh jr, yql tvs frpkl trrq iwql rpb bvyb bvwt frpkl cs bvs cwjjstb owtbyhs tvs erpkl oyhs wq bvswu uskybwrqtvwx.""")

    print(data["plainText"])
    print(data["key"])

if __name__ == "__main__":
    main()

