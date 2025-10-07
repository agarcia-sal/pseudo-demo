from typing import List

def encode_shift(string: str) -> str:
    encoded_characters: List[str] = []
    for character in string:
        shifted_value = (ord(character) + 5 - ord('a')) % 26 + ord('a')
        shifted_character = chr(shifted_value)
        encoded_characters.append(shifted_character)
    encoded_string = ''.join(encoded_characters)
    return encoded_string

def decode_shift(string: str) -> str:
    decoded_characters: List[str] = []
    for character in string:
        shifted_value = (ord(character) - 5 - ord('a')) % 26 + ord('a')
        shifted_character = chr(shifted_value)
        decoded_characters.append(shifted_character)
    decoded_string = ''.join(decoded_characters)
    return decoded_string