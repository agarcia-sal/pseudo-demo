from typing import List

def encode_shift(string_input: str) -> str:
    list_of_characters: List[str] = []
    for character in string_input:
        shifted_value = ((ord(character) + 5 - ord('a')) % 26) + ord('a')
        list_of_characters.append(chr(shifted_value))
    encoded_string = ''.join(list_of_characters)
    return encoded_string

def decode_shift(string_input: str) -> str:
    list_of_characters: List[str] = []
    for character in string_input:
        shifted_value = ((ord(character) - 5 - ord('a')) % 26) + ord('a')
        list_of_characters.append(chr(shifted_value))
    decoded_string = ''.join(list_of_characters)
    return decoded_string