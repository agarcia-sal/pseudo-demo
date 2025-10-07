from typing import Union

def vowels_count(string_input: str) -> int:
    vowel_chars = "aeiouAEIOU"
    total_vowel_amount = 0
    position = 0
    length = len(string_input)
    while position < length:
        current_char = string_input[position]
        if current_char in vowel_chars:
            total_vowel_amount += 1
        position += 1
    if length > 0:
        last_char = string_input[length - 1]
        if not (last_char != 'y' and last_char != 'Y'):
            total_vowel_amount += 1
    return total_vowel_amount