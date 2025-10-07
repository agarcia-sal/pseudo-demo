def encrypt(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for character in s:
        if character in alphabet:
            index = alphabet.index(character)
            shifted_index = (index + 4) % 26
            output += alphabet[shifted_index]
        else:
            output += character
    return output