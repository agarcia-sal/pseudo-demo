from typing import Literal


def vowels_count(string_input: str) -> int:
    vowel_chars: str = "aeiouAEIOU"
    count_vowels: int = 0
    index: int = 0
    length: int = len(string_input)
    while index < length:
        if string_input[index] in vowel_chars:
            count_vowels += 1
        index += 1
    if length > 0 and string_input[-1] in ('y', 'Y'):
        count_vowels += 1
    return count_vowels