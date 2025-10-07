def encrypt(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for c in s:
        if c in alphabet:
            index = alphabet.index(c)
            new_index = (index + 4) % 26
            output += alphabet[new_index]
        else:
            output += c
    return output