from typing import List


def encode_shift(input_string: str) -> str:
    encoded_characters: List[str] = []
    for character in input_string:
        if 'a' <= character <= 'z':
            shifted_value = ((ord(character) + 5) - ord('a')) % 26 + ord('a')
            encoded_characters.append(chr(shifted_value))
        else:
            # Preserve characters outside 'a'-'z' as is
            encoded_characters.append(character)
    return ''.join(encoded_characters)


def decode_shift(input_string: str) -> str:
    decoded_characters: List[str] = []
    for character in input_string:
        if 'a' <= character <= 'z':
            shifted_value = ((ord(character) - 5) - ord('a')) % 26 + ord('a')
            decoded_characters.append(chr(shifted_value))
        else:
            # Preserve characters outside 'a'-'z' as is
            decoded_characters.append(character)
    return ''.join(decoded_characters)