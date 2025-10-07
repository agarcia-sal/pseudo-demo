from typing import List


def vowels_count(text_arg: str) -> int:
    vowel_collection: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count_vowels: int = 0
    for letter in text_arg:
        if letter in vowel_collection:
            count_vowels += 1
    if text_arg.endswith(('y', 'Y')):
        count_vowels += 1
    return count_vowels