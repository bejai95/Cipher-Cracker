# This program will decode a Caesar Cipher
# It uses some code/ideas from https://inventwithpython.com/hacking/chapter7.html

from detectEnglish import isEnglish

UPPER_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Later put these somwehere else?
LOWER_ALPHABET = UPPER_ALPHABET.lower()
NUM_LETTTERS_IN_ALPHABET = 26

def caesarHacker(cipherText):
    for potentialKey in range(NUM_LETTTERS_IN_ALPHABET):
        potentialString = [] # Apprarently it is more efficient in python to build strings like this

        for character in cipherText:
            if character in UPPER_ALPHABET or character in LOWER_ALPHABET: # Don't decrypt non-alphabetical characters
                
                if character in UPPER_ALPHABET:
                    originalPosition = UPPER_ALPHABET.find(character)
                    newPosition = (originalPosition - potentialKey) % 26
                    potentialString.append(UPPER_ALPHABET[newPosition])
                else:
                    originalPosition = LOWER_ALPHABET.find(character)
                    newPosition = (originalPosition - potentialKey) % 26
                    potentialString.append(LOWER_ALPHABET[newPosition])
            
            else:
                potentialString.append(character)
        
        potentialString = ''.join(potentialString)

        if isEnglish(potentialString):
            return {
                "plainText": potentialString,
                "key": potentialKey
            }
    
    return {
        "message": "Sorry, could not decrypt the cipherText as a Caesar cipher, maybe try decrypting as a Transposition or Substitution cipher instead",
    }