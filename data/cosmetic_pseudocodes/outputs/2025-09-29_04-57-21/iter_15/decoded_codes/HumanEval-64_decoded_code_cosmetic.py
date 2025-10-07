from typing import Literal

def vowels_count(string_input: str) -> int:
    vowel_chars: Literal["AEIOUaeiou"] = "AEIOUaeiou"
    count_vowels: int = 0
    position: int = 0

    while position < len(string_input):
        current_char: str = string_input[position]
        if current_char in vowel_chars:
            count_vowels += 1
        position += 1

    last_index: int = len(string_input) - 1
    if last_index >= 0 and not (string_input[last_index] != 'y' and string_input[last_index] != 'Y'):
        count_vowels += 1

    return count_vowels