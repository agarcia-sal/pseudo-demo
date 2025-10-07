from typing import Literal

def vowels_count(string_input: str) -> int:
    permitted_vowels: Literal["AEIOUaeiou"] = "AEIOUaeiou"
    vowel_counter: int = 0
    idx: int = 0
    length: int = len(string_input)
    while idx < length:
        curr_char: str = string_input[idx]
        if curr_char in permitted_vowels:
            vowel_counter += 1
        idx += 1

    if length > 0:
        terminal_char: str = string_input[length - 1]
        if terminal_char == 'Y' or terminal_char == 'y':
            vowel_counter += 1

    return vowel_counter