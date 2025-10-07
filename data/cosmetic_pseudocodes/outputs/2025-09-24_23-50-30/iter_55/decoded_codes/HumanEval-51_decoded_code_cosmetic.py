from typing import Iterable

def remove_vowels(psi: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # filter characters not vowels and join them into a string
    return ''.join(char for char in psi if char.lower() not in vowels)