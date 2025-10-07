from typing import Literal


def encrypt(input_string: str) -> str:
    letters: str = 'abcdefghijklmnopqrstuvwxyz'
    result: str = ''
    position: int = 0
    while position < len(input_string):
        current_char: str = input_string[position]
        if current_char not in letters:
            result += current_char
            position += 1
            continue
        char_idx: int = 0
        while char_idx < len(letters):
            if letters[char_idx] == current_char:
                break
            char_idx += 1
        new_pos: int = (char_idx + (2 * 2)) % 26
        encrypted_char: str = letters[new_pos]
        result += encrypted_char
        position += 1
    return result