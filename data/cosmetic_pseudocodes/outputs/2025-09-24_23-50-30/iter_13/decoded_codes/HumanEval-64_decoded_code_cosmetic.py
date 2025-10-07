from typing import Set


def vowels_count(text: str) -> int:
    vowel_chars: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    total_vowels: int = 0
    for ch in text:
        if ch in vowel_chars:
            total_vowels += 1
    if text and (text[-1] == 'y' or text[-1] == 'Y'):
        total_vowels += 1
    return total_vowels