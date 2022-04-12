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
    bestKey = getKeyBeforeFullDecipher(intersectedMapping)
    totalAmountPossibilities = getTotalAmountPossibilities
    
    answer = input("To solve this substitution cipher completely, would need to try " + str(totalAmountPossibilities) + " possible keys. Type 'full' to fully decipher, or leave blank to just show what has already been worked out:\n")

    if answer == "full":
        bestKey = fullDecipher(cipherText, intersectedMapping)
        
    return {
        "plainText": decrypt(cipherText, bestKey),
        "key": bestKey
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

def main():
    data = substitutionHacker("""Pkry ldi'e npqntd n cnt kf dgidwliy. Ewne'd qwne ewy kpjyc olcpd myue eypplio wyc qwyi dwy dnlj dwy wnj fkgij ewy uycfyae xni. Dwy wnj ewkgowe ewld qnd dlxupt bleeyc enpm ki ewylc unce dliay ewyt wnj byyi ginbpy ek flij ecgy pkry plmy wycd. Bge ikq dwy wnj ek fnay ewy fnae ewne ewyt xnt wnry byyi clowe. Pkry xnt ike npqntd by n cnt kf dgidwliy. Ewne ld gipydd ewyt qycy cyfycclio ek wkq ewy dgi ani bgci.

Wkq wnj dwy byyi dk qckio? Npp wyc lideliaed nij lieglelki akxupyeypt fnlpyj wyc fkc ewy flcde elxy li wyc plfy. Dwy wnj dk wynrlpt cyplyj ki bkew qwyi xnmlio jyaldlkid gu gielp ewld xkxyie nij dwy fype n dyldxla dwlfe enmy upnay li wyc dypf-akifljyiay. Lf dwy akgpj by dk akxupyeypt qckio nbkge dkxyewlio dk dlxupy nd ewld, wkq akgpj dwy xnmy jyaldlkid nbkge cynppt lxukcenie ewliod enmlio upnay li wyc plfy? Dwy qndi'e dgcy qwne dwy dwkgpj jk iyse.

Ewy wynjuwkiyd qycy ki. Ewyt wnj byyi gelplhyj ki ugcukdy. Dwy akgpj wync wyc xkx typplio li ewy bnamockgij, bge akgpji'e xnmy kge ysnaept qwne ewy typplio qnd nbkge. Ewne qnd ysnaept qwt dwy wnj uge ewyx ki. Dwy miyq wyc xkx qkgpj yieyc wyc ckkx ne nit xligey, nij dwy akgpj ucyeyij ewne dwy wnji'e wyncj nit kf ewy ucyrlkgd typplio.

Ewycy qnd dkxyewlio duyalnp nbkge ewld pleepy acynegcy. Jkiin akgpji'e vgley uliuklie qwne le qnd, bge dwy miyq qlew npp wyc wynce ewne le qnd ecgy. Le qndi'e n xneeyc kf lf dwy qnd oklio ek ect nij dnry le, bge n xneeyc kf wkq dwy qnd oklio ek dnry le. Dwy qyie bnam ek ewy anc ek oye n bpnimye nij qwyi dwy cyegciyj ewy acynegcy qnd okiy.

Jnry qneawyj nd ewy fkcyde bgciyj gu ki ewy wlpp, kipt n fyq xlpyd fckx wyc wkgdy. Ewy anc wnj byyi wndelpt unamyj nij Xncen qnd lidljy ectlio ek ckgij gu ewy pnde kf ewy uyed. Jnry qyie ewckgow wld xyienp plde kf ewy xkde lxukcenie unuycd nij jkagxyied ewne ewyt akgpji'e pynry bywlij. Wy dakpjyj wlxdypf fkc ike wnrlio ucyuncyj ewydy byeeyc li njrniay nij wkuyj ewne wy wnj cyxyxbycyj yryctewlio ewne qnd iyyjyj. Wy akieligyj ek qnle fkc Xncen ek nuuync qlew ewy uyed, bge dwy delpp qnd ikqwycy ek by dyyi.
""")

    print(data["plainText"])
    print(data["key"])

if __name__ == "__main__":
    main()