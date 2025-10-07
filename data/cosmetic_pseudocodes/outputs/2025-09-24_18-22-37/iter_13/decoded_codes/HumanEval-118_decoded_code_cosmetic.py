from typing import Set

def get_closest_vowel(input_string: str) -> str:
    result_string: str = ""
    if len(input_string) < 3:
        return result_string

    vowel_chars: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    pos: int = len(input_string) - 2
    while pos >= 1:
        current_char: str = input_string[pos]
        if current_char in vowel_chars:
            next_char: str = input_string[pos + 1]
            prev_char: str = input_string[pos - 1]
            if (next_char not in vowel_chars) and (prev_char not in vowel_chars):
                return current_char
        pos -= 1

    return result_string