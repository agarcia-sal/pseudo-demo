from typing import Iterator


def encrypt(input_string: str) -> str:
    letters: str = 'abcdefghijklmnopqrstuvwxyz'
    result: str = ''
    iterator: int = 0

    while iterator < len(input_string):
        current_char: str = input_string[iterator]

        if current_char in letters:
            original_pos: int = letters.index(current_char)
            new_pos: int = (original_pos + 4) % 26  # 2 * 2 = 4
            result += letters[new_pos]
            iterator += 1
            continue

        result += current_char
        iterator += 1

    return result