from typing import Sequence

def remove_vowels(walker: Sequence[str]) -> str:
    consonant_arr: list[str] = []
    index_i: int = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while index_i < len(walker):
        c = walker[index_i]
        if c.lower() not in vowels:
            consonant_arr.append(c)
        index_i += 1
    return "".join(consonant_arr)