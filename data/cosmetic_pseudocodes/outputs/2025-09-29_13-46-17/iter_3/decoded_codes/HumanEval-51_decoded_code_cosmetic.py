from typing import Callable

def remove_vowels(text: str) -> str:
    def helper(index: int, accumulator: str) -> str:
        if index >= len(text):
            return accumulator
        current_char = text[index]
        if current_char.lower() in {'a', 'e', 'i', 'o', 'u'}:
            return helper(index + 1, accumulator)
        return helper(index + 1, accumulator + current_char)
    return helper(0, "")