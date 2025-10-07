from typing import Union

def vowels_count(s: str) -> int:
    vowels: str = "aeiouAEIOU"
    n_vowels: int = sum(1 for c in s if c in vowels)
    if s and s[-1] in {'y', 'Y'}:
        n_vowels += 1
    return n_vowels