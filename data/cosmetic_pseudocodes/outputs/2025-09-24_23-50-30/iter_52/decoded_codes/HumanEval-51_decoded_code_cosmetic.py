from typing import Callable

def remove_vowels(item: str) -> str:
    def helper(index: int, accumulator: str) -> str:
        if index >= len(item):
            return accumulator
        # Check if the current character is a vowel (case-insensitive)
        if item[index].lower() in {'a', 'e', 'i', 'o', 'u'}:
            return helper(index + 1, accumulator)
        else:
            return helper(index + 1, accumulator + item[index])
    return helper(0, "")