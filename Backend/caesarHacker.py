# This program will decode a Caesar Cipher
# It uses some code from https://inventwithpython.com/hacking/chapter7.html

from email import message
from detectEnglish import isEnglish

CYPHERTEXT = "GUVF VF ZL FRPERG ZRFFNTR." # TODO: Delete this later

UPPER_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Later put these somwehere else?
LOWER_ALPHABET = UPPER_ALPHABET.lower()
NUM_LETTTERS_IN_ALPHABET = 26

def caesarHacker(cipherText):
    for potentialKey in range(NUM_LETTTERS_IN_ALPHABET):
        potentialString = ''

        for character in cipherText:
            if character in UPPER_ALPHABET or character in LOWER_ALPHABET: # Don't decrypt non-alphabetical characters
                
                if character in UPPER_ALPHABET:
                    originalPosition = UPPER_ALPHABET.find(character)
                    newPosition = (originalPosition - potentialKey) % 26
                    potentialString = potentialString + UPPER_ALPHABET[newPosition]
                else:
                    originalPosition = LOWER_ALPHABET.find(character)
                    newPosition = (originalPosition - potentialKey) % 26
                    potentialString = potentialString + LOWER_ALPHABET[newPosition]
            
            else:
                potentialString = potentialString + character
        
        if (isEnglish(potentialString)):
            return {
                "plainText": potentialString,
                "key": potentialKey
            }
    
    return {
        "error": "Something went wrong :("
    }
    
def main():
    try:
        plainText = caesarHacker(CYPHERTEXT)["plainText"]
        print(plainText)
    except:
        error = caesarHacker(CYPHERTEXT)["error"]
        print(error)

if __name__ == '__main__':
    main()