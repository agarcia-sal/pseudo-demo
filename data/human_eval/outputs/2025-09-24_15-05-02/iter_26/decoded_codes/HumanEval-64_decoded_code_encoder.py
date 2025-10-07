from typing import Union


def vowels_count(string_word: str) -> int:
    vowels: str = "aeiouAEIOU"
    number_of_vowels: int = sum(char in vowels for char in string_word)
    if string_word and string_word[-1] in ('y', 'Y'):
        number_of_vowels += 1
    return number_of_vowels