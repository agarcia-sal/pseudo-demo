from typing import Callable

def vowels_count(str_param: str) -> int:
    letters_collection: str = "aeiouAEIOU"

    def count_chars(index: int) -> int:
        if index >= len(str_param):
            return 0
        return (1 if str_param[index] in letters_collection else 0) + count_chars(index + 1)

    total_vowels: int = count_chars(0)

    if str_param[-1] in ('y', 'Y'):
        total_vowels += 1

    return total_vowels