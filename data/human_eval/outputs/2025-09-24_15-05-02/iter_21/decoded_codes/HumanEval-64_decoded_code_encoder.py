from typing import Union

def vowels_count(string: Union[str, bytes]) -> int:
    vowels: str = "aeiouAEIOU"
    number_of_vowels: int = 0
    for character in string:
        if character in vowels:
            number_of_vowels += 1
    if string and string[-1] in {'y', 'Y'}:
        number_of_vowels += 1
    return number_of_vowels