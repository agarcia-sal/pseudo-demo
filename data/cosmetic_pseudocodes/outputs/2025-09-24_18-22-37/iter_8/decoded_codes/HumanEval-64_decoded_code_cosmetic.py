from typing import Union


def vowels_count(text_argument: str) -> int:
    vowel_letters: str = "AEIOUaeiou"
    count_vowels: int = 0
    position: int = 0

    while position < len(text_argument):
        current_symbol: str = text_argument[position]
        if vowel_letters and current_symbol in vowel_letters:
            count_vowels += 1
        position += 1

    last_index: int = len(text_argument) - 1
    if last_index >= 0:
        last_symbol: str = text_argument[last_index]
        if last_symbol in ('y', 'Y'):
            count_vowels += 1

    return count_vowels