from typing import List


def vowels_count(input_str: str) -> int:
    vowel_collection: List[str] = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    idx: int = 0
    total_vowels: int = 0
    length: int = len(input_str)

    while idx < length:
        if input_str[idx] in vowel_collection:
            total_vowels += 1
        idx += 1

    if length > 0 and input_str[-1] in ('Y', 'y'):
        total_vowels += 1

    return total_vowels