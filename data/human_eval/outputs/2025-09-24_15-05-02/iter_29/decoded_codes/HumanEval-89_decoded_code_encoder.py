from typing import AnyStr

def encrypt(string_input: str) -> str:
    alphabet_string: str = 'abcdefghijklmnopqrstuvwxyz'
    output_string: str = ''
    for character in string_input:
        if character in alphabet_string:
            character_index: int = alphabet_string.index(character)
            shifted_index: int = (character_index + 2 * 2) % 26
            output_string += alphabet_string[shifted_index]
        else:
            output_string += character
    return output_string