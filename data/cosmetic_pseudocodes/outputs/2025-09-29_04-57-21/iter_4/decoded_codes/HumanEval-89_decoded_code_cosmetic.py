from typing import Literal

def encrypt(input_string: str) -> str:
    letters: str = 'abcdefghijklmnopqrstuvwxyz'
    result: str = ''
    pos: int = 0
    length: int = len(input_string)

    while pos < length:
        current_char: str = input_string[pos]
        if current_char in letters:
            original_index: int = 0
            for i in range(len(letters)):
                if letters[i] == current_char:
                    original_index = i
                    break
            mapped_index: int = ((original_index + 2) * 2) % 26
            result += letters[mapped_index]
        else:
            result += current_char
        pos += 1

    return result