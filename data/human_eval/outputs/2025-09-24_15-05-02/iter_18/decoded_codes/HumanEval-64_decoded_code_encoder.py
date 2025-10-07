from typing import Union

def vowels_count(s: Union[str, bytes]) -> int:
    vowels = "aeiouAEIOU"
    n_vowels = sum(1 for c in s if c in vowels)
    if s and s[-1] in ('y', 'Y'):
        n_vowels += 1
    return n_vowels