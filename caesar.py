#returns alphabet position of a letter- assumes letter as input
def alphabet_position(letter):
    #check for capitals
    if letter.isupper():
        #if capital subtract ascii value of A to find alphabet position
        return ord(letter) - ord('A')
    else:
        #otherwise subtract ascii value of 'a' to find position
        return ord(letter) - ord('a')
#rotates character to the right by amount specified
def rotate_character(char, rot):
    #checks if char being called upon is a letter
    if char.isalpha():
        #uses modulo to rotate back to 'a' if needed, then adjusts letter case
        rotated = (alphabet_position(char) + rot) % 26 \
                + ord(char) - alphabet_position(char)
        #returns char associated with ordinal value calculated
        return chr(rotated)
    #if not a letter, returns as is
    else:
        return char

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        encrypted = encrypted + rotate_character(char, rot)
    return encrypted
