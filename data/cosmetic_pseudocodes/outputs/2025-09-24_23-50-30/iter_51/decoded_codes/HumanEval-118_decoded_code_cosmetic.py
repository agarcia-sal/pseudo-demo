from typing import Callable

def get_closest_vowel(input_string: str) -> str:
    vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def scan(position: int) -> str:
        if position < 1:
            return ""
        current_char = input_string[position]
        if current_char in vowel_set:
            prev_char = input_string[position - 1]
            next_char = input_string[position + 1]
            if not (prev_char in vowel_set or next_char in vowel_set):
                return current_char
        return scan(position - 1)

    if len(input_string) < 3:
        return ""
    return scan(len(input_string) - 2)