def encrypt(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(alphabet[(alphabet.index(c) + 4) % 26] if c in alphabet else c for c in input_string)