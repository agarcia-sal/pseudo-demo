from typing import Union

def encrypt(string_input: str) -> str:
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    output_string: str = ''
    for character in string_input:
        if character in alphabet:
            shifted_index: int = (alphabet.index(character) + 4) % 26
            output_string += alphabet[shifted_index]
        else:
            output_string += character
    return output_string