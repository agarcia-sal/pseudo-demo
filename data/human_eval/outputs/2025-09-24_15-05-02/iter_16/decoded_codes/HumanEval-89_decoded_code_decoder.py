from typing import Union

def encrypt(input_string: str) -> str:
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    output_string: str = ''
    for character in input_string:
        if character in alphabet:
            shifted_index: int = (alphabet.index(character) + 4) % 26
            output_string += alphabet[shifted_index]
        else:
            output_string += character
    return output_string