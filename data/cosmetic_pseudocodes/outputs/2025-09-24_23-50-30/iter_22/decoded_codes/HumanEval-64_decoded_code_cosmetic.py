from typing import Set

def vowels_count(text: str) -> int:
    vowel_set: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count_accumulator: int = 0
    for index in range(len(text)):
        letter: str = text[index]
        if letter in vowel_set:
            count_accumulator += 1
    if text and text[-1] in {'y', 'Y'}:
        count_accumulator += 1
    return count_accumulator