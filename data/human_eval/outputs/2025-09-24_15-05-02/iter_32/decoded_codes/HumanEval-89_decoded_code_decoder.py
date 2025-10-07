from typing import Union

def encrypt(string_input: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output_string = []
    for character in string_input:
        if character in alphabet:
            rotated_index = (alphabet.index(character) + 4) % 26
            output_string.append(alphabet[rotated_index])
        else:
            output_string.append(character)
    return ''.join(output_string)