from typing import Callable

def remove_vowels(alpha: str) -> str:
    def helper(index: int, result: str) -> str:
        if index >= len(alpha):
            return result
        current_char = alpha[index]
        lowered_char = current_char.lower()
        if lowered_char in {'a', 'e', 'i', 'o', 'u'}:
            return helper(index + 1, result)
        else:
            return helper(index + 1, result + current_char)
    return helper(0, "")