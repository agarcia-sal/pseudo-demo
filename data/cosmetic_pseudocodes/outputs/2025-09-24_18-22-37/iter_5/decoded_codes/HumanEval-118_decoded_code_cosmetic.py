from typing import Literal

def get_closest_vowel(input_str: str) -> str:
    if len(input_str) < 3:
        return ""

    vowels_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    pos = len(input_str) - 2
    while pos >= 1:
        curr_char = input_str[pos]
        if curr_char in vowels_set:
            if (input_str[pos - 1] not in vowels_set) and (input_str[pos + 1] not in vowels_set):
                return curr_char
        pos -= 1

    return ""