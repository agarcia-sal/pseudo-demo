from typing import Callable

def vowels_count(string_input: str) -> int:
    vowel_chars: str = "AEIOUaeiou"

    def count_vowels_at(index: int) -> int:
        if index == len(string_input):
            return 0
        increment = 1 if string_input[index] in vowel_chars else 0
        return increment + count_vowels_at(index + 1)

    tally: int = count_vowels_at(0)

    if string_input and string_input[-1] in {'Y', 'y'}:
        tally += 1

    return tally