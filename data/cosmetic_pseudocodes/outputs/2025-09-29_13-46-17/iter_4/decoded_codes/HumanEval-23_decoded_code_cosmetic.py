from typing import Callable

def strlen(text_input: str) -> int:
    total_chars = 0

    def count_characters(index: int) -> int:
        nonlocal total_chars
        if index == len(text_input):
            return total_chars
        total_chars += 1
        return count_characters(index + 1)

    return count_characters(0)