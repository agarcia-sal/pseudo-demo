from typing import List


def vowels_count(string_input: str) -> int:
    vowel_chars: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    total_vowels: int = 0
    for index in range(len(string_input)):
        if string_input[index] in vowel_chars:
            total_vowels += 1
    if string_input[-1] in {'y', 'Y'}:
        total_vowels += 1
    return total_vowels