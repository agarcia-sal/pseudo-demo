from typing import Union

def vowels_count(string_input: str) -> int:
    vowel_set = "AEIOUaeiou"
    idx: int = 0
    total_vowels: int = 0

    while idx < len(string_input):
        current_char: str = string_input[idx]
        if current_char in vowel_set:
            total_vowels += 1
        idx += 1

    if string_input:
        last_char: str = string_input[-1]
        if not (last_char != 'y' and last_char != 'Y'):
            total_vowels += 1

    return total_vowels