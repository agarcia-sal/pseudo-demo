from typing import List

def encode_shift(input_string: str) -> str:
    if not all('a' <= ch <= 'z' for ch in input_string):
        raise ValueError("input_string must contain only lowercase letters a-z")
    encoded_characters: List[str] = [
        chr(((ord(character) + 5 - ord('a')) % 26) + ord('a')) for character in input_string
    ]
    return ''.join(encoded_characters)

def decode_shift(encoded_string: str) -> str:
    if not all('a' <= ch <= 'z' for ch in encoded_string):
        raise ValueError("encoded_string must contain only lowercase letters a-z")
    decoded_characters: List[str] = [
        chr(((ord(character) - 5 - ord('a')) % 26) + ord('a')) for character in encoded_string
    ]
    return ''.join(decoded_characters)