# This module can be used to get the 'word pattern' of a word, and also to create the allWordPatterns.py file
# It uses some code/ideas from https://inventwithpython.com/hacking/chapter18.html

import pprint

def getWordPattern(word):
    word = word.lower()
    nextNum = 0
    letterNums = {}
    wordPattern = []

    for character in word:
        if character != '\'':
            if character not in letterNums:
                letterNums[character] = str(nextNum)
                nextNum += 1
            wordPattern.append(letterNums[character])
        else:
            wordPattern.append('\'') # We want it to show the apostrophe rather than a number

    return '.'.join(wordPattern)

def createAllWordPatternsFile():
    allWordPatterns = {}
    dictionaryFile = open('dictionary.txt', "r")
    wordList =  dictionaryFile.read().split('\n')
    dictionaryFile.close()

    for word in wordList:
        wordPattern = getWordPattern(word)

        if wordPattern not in allWordPatterns:
            allWordPatterns[wordPattern] = [word]
        else:
            allWordPatterns[wordPattern].append(word)

    # Now that we have our allWordPatterns dictionary, we want to write it onto the python file allWordPatternsDictionary.py
    # This is code that writes more code
    allWordPatternsFile = open('allWordPatterns.py', "w")
    allWordPatternsFile.write('# This file was written by wordPatternsGeneral.createAllWordPatternsFile()\n\n')
    allWordPatternsFile.write('allWordPatterns = ')
    allWordPatternsFile.write(pprint.pformat(allWordPatterns))
    allWordPatternsFile.close()

    return