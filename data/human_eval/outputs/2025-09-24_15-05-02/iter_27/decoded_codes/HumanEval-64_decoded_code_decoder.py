from typing import Union


def vowels_count(input_string: str) -> int:
    vowels: str = "aeiouAEIOU"
    number_of_vowels: int = sum(1 for char in input_string if char in vowels)
    if input_string and input_string[-1] in {'y', 'Y'}:
        number_of_vowels += 1
    return number_of_vowels