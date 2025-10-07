from typing import List


def vowels_count(input_string: str) -> int:
    vowel_chars: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def count_vowels_at(index: int, tally: int) -> int:
        if index >= len(input_string):
            return tally
        increment = 1 if input_string[index] in vowel_chars else 0
        return count_vowels_at(index + 1, tally + increment)

    total_vowels: int = count_vowels_at(0, 0)

    if input_string[-1:] in {'y', 'Y'}:
        total_vowels += 1

    return total_vowels