def encrypt(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for character in s:
        if character in alphabet:
            originalIndex = alphabet.index(character)
            shiftedIndex = (originalIndex + 2 * 2) % 26
            output += alphabet[shiftedIndex]
        else:
            output += character
    return output