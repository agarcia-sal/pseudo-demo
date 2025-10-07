from typing import List


def check_if_last_char_is_a_letter(input_string: str) -> bool:
    def is_ascii_alpha(character: str) -> bool:
        # Check if character is a lowercase ASCII letter
        return 97 <= ord(character) <= 122

    words_array: List[str] = input_string.split(" ")
    if not words_array:
        return False  # No words in input string

    final_token: str = words_array[-1]

    if len(final_token) == 1:
        # Guard clause: if length of final_token is exactly 1, return False
        return False

    # Check if last token lowercased is a lowercase ASCII letter
    return is_ascii_alpha(final_token.lower())