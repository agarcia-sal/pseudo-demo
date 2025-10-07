from typing import Callable

def vowels_count(string_input: str) -> int:
    VOWEL_CHARS: str = "AEIOUaeiou"

    def count_vowels_in(index: int, acc: int) -> int:
        if index == len(string_input):
            return acc
        if string_input[index] in VOWEL_CHARS:
            return count_vowels_in(index + 1, acc + 1)
        return count_vowels_in(index + 1, acc)

    tally: int = count_vowels_in(0, 0)
    if not (string_input[-1] != 'y' and string_input[-1] != 'Y'):
        tally += 1
    return tally