from typing import Union

def encrypt(input_string: str) -> str:
    letters: str = 'abcdefghijklmnopqrstuvwxyz'
    result_string: str = ''
    position: int = 0
    while position < len(input_string):
        current_char: str = input_string[position]
        if current_char in letters:
            initial_pos: int = letters.index(current_char)
            computed_pos: int = (initial_pos + 4) % 26
            result_string += letters[computed_pos]
        else:
            result_string += current_char
        position += 1
    return result_string