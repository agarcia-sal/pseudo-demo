from typing import Union

def vowels_count(string_input: str) -> int:
    vowels = "aeiouAEIOU"
    number_of_vowels = sum(char in vowels for char in string_input)
    if string_input and string_input[-1] in ('y', 'Y'):
        number_of_vowels += 1
    return number_of_vowels