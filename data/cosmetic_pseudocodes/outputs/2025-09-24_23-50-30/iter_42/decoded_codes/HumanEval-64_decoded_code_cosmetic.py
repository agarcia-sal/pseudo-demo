from typing import Callable

def vowels_count(input_string: str) -> int:
    def count_vowels(position: int, total: int) -> int:
        if position == len(input_string):
            # Add 1 if last character is 'y' or 'Y'
            return total + (1 if input_string[position - 1] in ('y', 'Y') else 0)
        if input_string[position] in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
            return count_vowels(position + 1, total + 1)
        return count_vowels(position + 1, total)
    return count_vowels(0, 0)