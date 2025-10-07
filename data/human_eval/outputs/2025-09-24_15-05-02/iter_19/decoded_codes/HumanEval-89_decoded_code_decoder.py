from typing import Final

def encrypt(input_string: str) -> str:
    alphabet: Final[str] = 'abcdefghijklmnopqrstuvwxyz'
    output_string: str = ''
    for character in input_string:
        if character in alphabet:
            original_index: int = alphabet.index(character)
            shifted_index: int = (original_index + 4) % 26
            output_string += alphabet[shifted_index]
        else:
            output_string += character
    return output_string