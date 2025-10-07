from typing import List


def encode_shift(input_string: str) -> str:
    encoded_characters: List[str] = []
    position: int = 0
    while position < len(input_string):
        current_char: str = input_string[position]
        numeric_value: int = ord(current_char) - ord('a')
        shifted_value: int = (numeric_value + 5) % 26
        transformed_char: str = chr(shifted_value + ord('a'))
        encoded_characters.append(transformed_char)
        position += 1
    return ''.join(encoded_characters)


def decode_shift(input_string: str) -> str:
    decoded_chars: List[str] = []
    idx: int = 0
    while idx < len(input_string):
        letter: str = input_string[idx]
        letter_num: int = ord(letter) - ord('a')
        reversed_shift: int = (letter_num - 5) % 26
        new_char: str = chr(reversed_shift + ord('a'))
        decoded_chars.append(new_char)
        idx += 1
    return ''.join(decoded_chars)