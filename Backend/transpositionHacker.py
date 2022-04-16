# This program will decode a transposition cipher (using the grid method of transposition) -> Plesase see the description for this method of transposition encryption given at the top of https://inventwithpython.com/hacking/chapter8.html

# This program uses some code/ideas from https://inventwithpython.com/hacking/chapter9.html

from detectEnglish import isEnglish
import math

def transpositionHacker(cipherText):
    for potentialKey in range(1, len(cipherText)):
        potentialString = decrypt(cipherText, potentialKey)

        if isEnglish(potentialString):

            return {
                "plainText": potentialString,
                "key": potentialKey
            }
    
    return {
        "message": "Sorry, could not decrypt the ciphertext as a Transposition cipher, maybe try decrypting as a Caesar or Substitution cipher instead.",
    }

def decrypt(cipherText, key):
    
    # Create a grid, with 'shaded boxes'
    numRows = key
    numCols = math.ceil(len(cipherText) / key)
    numShadedBoxes = (numCols * numRows) - len(cipherText)
    grid = [''] * numCols # Python is weird, this actually creates an array like ['','','','','']
    currentRow = 0
    currentCol = 0

    for character in cipherText:
        grid[currentCol] += character
        currentCol += 1

        # If we are now over the edge of the grid or on a 'shaded box', move to the next row
        if (currentCol == numCols) or (currentCol == numCols - 1 and currentRow >= numRows - numShadedBoxes):
            currentCol = 0
            currentRow += 1

    return ''.join(grid)