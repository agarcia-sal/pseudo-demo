from typing import Optional


def encrypt(string_input: str) -> str:
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    output_string: list[str] = []
    for character in string_input:
        if character in alphabet:
            original_index: int = alphabet.index(character)
            shifted_index: int = (original_index + 4) % 26
            shifted_character: str = alphabet[shifted_index]
            output_string.append(shifted_character)
        else:
            output_string.append(character)
    return ''.join(output_string)