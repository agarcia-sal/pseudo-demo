def encrypt(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""

    for character in s:
        if character in alphabet:
            original_index = alphabet.index(character)
            shifted_index = (original_index + 4) % 26
            shifted_character = alphabet[shifted_index]
            output += shifted_character
        else:
            output += character

    return output