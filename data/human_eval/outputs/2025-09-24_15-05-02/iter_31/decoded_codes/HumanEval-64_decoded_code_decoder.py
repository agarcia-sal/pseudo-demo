from typing import Union

def vowels_count(input_string: str) -> int:
    vowels = "aeiouAEIOU"
    number_of_vowels = sum(char in vowels for char in input_string)
    if input_string and input_string[-1] in {'y', 'Y'}:
        number_of_vowels += 1
    return number_of_vowels