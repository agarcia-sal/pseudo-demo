from typing import Union


def vowels_count(string_input: str) -> int:
    vowel_chars = "AEIOUaeiou"
    total_vowels = 0
    for index in range(1, len(string_input) + 1):
        current_char = string_input[index - 1]  # Adjust for zero-based indexing
        if current_char in vowel_chars:
            total_vowels += 1

    if string_input and string_input[-1] in {'y', 'Y'}:
        total_vowels += 1

    return total_vowels