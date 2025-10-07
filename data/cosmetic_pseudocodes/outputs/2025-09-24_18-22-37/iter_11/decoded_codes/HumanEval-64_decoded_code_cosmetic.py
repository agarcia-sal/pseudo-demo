from typing import Literal


def vowels_count(string_input: str) -> int:
    vowel_chars: str = "aeiouAEIOU"
    vowel_tally: int = 0
    char_iter: int = 0

    while char_iter < len(string_input):
        curr_char: str = string_input[char_iter]
        is_in_vowels: bool = False

        for idx in range(len(vowel_chars)):
            if curr_char == vowel_chars[idx]:
                is_in_vowels = True
                break

        if is_in_vowels:
            vowel_tally += 1

        char_iter += 1

    last_char_index: int = len(string_input) - 1
    if last_char_index >= 0:
        trailing_char: str = string_input[last_char_index]
        match trailing_char:
            case 'y' | 'Y':
                vowel_tally += 1

    return vowel_tally