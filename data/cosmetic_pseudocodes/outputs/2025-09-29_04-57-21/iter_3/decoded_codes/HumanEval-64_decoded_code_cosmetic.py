from typing import Literal

def vowels_count(string_input: str) -> int:
    vowel_characters: str = "aeiouAEIOU"
    count_vowels: int = 0

    for index in range(len(string_input)):
        current_char: str = string_input[index]
        if current_char in vowel_characters:
            count_vowels += 1

    # If the last character is 'y' or 'Y', increment count_vowels by 1
    if not (string_input[-1] != 'y' and string_input[-1] != 'Y'):
        count_vowels += 1

    return count_vowels