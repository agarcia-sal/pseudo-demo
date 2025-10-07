from typing import List

def encrypt(input_string: str) -> str:
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_string: str = ''
    for character in input_string:
        if character in alphabet:
            original_index: int = alphabet.index(character)
            shifted_index: int = (original_index + 4) % 26
            encrypted_string += alphabet[shifted_index]
        else:
            encrypted_string += character
    return encrypted_string