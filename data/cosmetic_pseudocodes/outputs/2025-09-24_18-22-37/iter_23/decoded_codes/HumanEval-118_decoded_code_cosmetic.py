from typing import Set


def get_closest_vowel(input_string: str) -> str:
    result_string: str = ""

    str_length: int = len(input_string)

    if str_length < 3:
        return result_string

    vowel_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    cursor: int = str_length - 2  # str_length - (1 + 1)

    while cursor >= 1:
        char_at_cursor: str = input_string[cursor]

        if char_at_cursor in vowel_set:
            left_char: str = input_string[cursor - 1]
            right_char: str = input_string[cursor + 1]

            left_is_vowel: bool = left_char in vowel_set
            right_is_vowel: bool = right_char in vowel_set

            if not right_is_vowel and not left_is_vowel:
                return char_at_cursor

        cursor -= 1

    return result_string