from typing import List

def encode_shift(string_input: str) -> str:
    encoded_string: str = ""
    for character in string_input:
        # Assuming input consists of lowercase letters a-z
        shifted_value = ((ord(character) + 5 - ord('a')) % 26) + ord('a')
        encoded_string += chr(shifted_value)
    return encoded_string

def decode_shift(string_input: str) -> str:
    decoded_string: str = ""
    for character in string_input:
        # Assuming input consists of lowercase letters a-z
        shifted_value = ((ord(character) - 5 - ord('a')) % 26) + ord('a')
        decoded_string += chr(shifted_value)
    return decoded_string