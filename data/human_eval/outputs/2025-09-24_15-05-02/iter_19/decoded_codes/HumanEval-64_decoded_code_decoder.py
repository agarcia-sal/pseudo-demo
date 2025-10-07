from typing import Union

def vowels_count(s: str) -> int:
    vowels: str = "aeiouAEIOU"
    count_vowels: int = 0
    for c in s:
        if c in vowels:
            count_vowels += 1
    if s and s[-1] in ('y', 'Y'):
        count_vowels += 1
    return count_vowels