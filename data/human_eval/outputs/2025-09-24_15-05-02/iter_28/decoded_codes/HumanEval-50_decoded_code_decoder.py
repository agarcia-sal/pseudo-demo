from typing import List

def encode_shift(string_input: str) -> str:
    encoded_characters: List[str] = []
    for character in string_input:
        shifted_value = ((ord(character) + 5 - ord('a')) % 26) + ord('a')
        encoded_characters.append(chr(shifted_value))
    return ''.join(encoded_characters)

def decode_shift(string_input: str) -> str:
    decoded_characters: List[str] = []
    for character in string_input:
        shifted_value = ((ord(character) - 5 - ord('a')) % 26) + ord('a')
        decoded_characters.append(chr(shifted_value))
    return ''.join(decoded_characters)