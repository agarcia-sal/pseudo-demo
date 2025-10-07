from typing import Literal


def encrypt(input_string: str) -> str:
    alphabet_chars: str = 'abcdefghijklmnopqrstuvwxyz'
    result_text: str = ''

    position_counter: int = 0
    while position_counter < len(input_string):
        current_char: str = input_string[position_counter]
        if current_char in alphabet_chars:
            base_index: int = 0
            found: bool = False
            while not found and base_index < len(alphabet_chars):
                if alphabet_chars[base_index] == current_char:
                    found = True
                else:
                    base_index += 1
            computed_index: int = (base_index + (2 * 2)) % 26
            result_text += alphabet_chars[computed_index]
        else:
            result_text += current_char
        position_counter += 1

    return result_text