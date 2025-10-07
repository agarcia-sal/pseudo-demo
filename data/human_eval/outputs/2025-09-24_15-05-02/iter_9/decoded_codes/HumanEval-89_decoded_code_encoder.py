def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = []
    for char in s:
        if char in alphabet:
            new_index = (alphabet.index(char) + 4) % 26
            output.append(alphabet[new_index])
        else:
            output.append(char)
    return ''.join(output)