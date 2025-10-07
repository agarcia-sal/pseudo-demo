from typing import Union

def vowels_count(string_s: str) -> int:
    vowels: str = "aeiouAEIOU"
    n_vowels: int = sum(char in vowels for char in string_s)
    if string_s and string_s[-1] in ('y', 'Y'):
        n_vowels += 1
    return n_vowels