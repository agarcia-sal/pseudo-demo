from typing import Callable

def vowels_count(string_input: str) -> int:
    VOWELS: str = "aeiouAEIOU"

    def is_vowel(char: str) -> int:
        # Returns 1 if char is in VOWELS, else 0
        return 1 if char in VOWELS else 0

    def count_vowels(in_str: str, idx: int) -> int:
        if idx == len(in_str):
            return 0
        return is_vowel(in_str[idx]) + count_vowels(in_str, idx + 1)

    total_vowels = count_vowels(string_input, 0)

    def add_y_if_ends_with_y(last_char: str) -> int:
        # Adds 1 if last_char is 'y' or 'Y', else 0
        if last_char == 'y' or last_char == 'Y':
            return total_vowels + 1
        return total_vowels

    if not string_input:
        return 0  # handle empty string edge case

    return add_y_if_ends_with_y(string_input[-1])