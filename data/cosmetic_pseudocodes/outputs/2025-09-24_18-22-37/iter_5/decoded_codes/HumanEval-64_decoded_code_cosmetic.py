from typing import Union


def vowels_count(text_param: str) -> int:
    vowels_collection: str = "aeiouAEIOU"
    total_vowels: int = 0
    index: int = 0
    length: int = len(text_param)
    while index < length:
        current_char: str = text_param[index]
        if current_char in vowels_collection:
            total_vowels += 1
        index += 1
    if length > 0 and text_param[-1] in {'y', 'Y'}:
        total_vowels += 1
    return total_vowels