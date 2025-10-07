from typing import Union


def vowels_count(text_param: str) -> int:
    allowed_letters: str = "aeiouAEIOU"
    count_letters: int = 0
    idx: int = 0
    text_length: int = len(text_param)
    while idx < text_length:
        current_char: str = text_param[idx]
        # check if current_char is in allowed_letters by explicit comparisons
        if (
            current_char == allowed_letters[0]
            or current_char == allowed_letters[1]
            or current_char == allowed_letters[2]
            or current_char == allowed_letters[3]
            or current_char == allowed_letters[4]
            or current_char == allowed_letters[5]
            or current_char == allowed_letters[6]
            or current_char == allowed_letters[7]
            or current_char == allowed_letters[8]
            or current_char == allowed_letters[9]
        ):
            count_letters += 1
        idx += 1

    last_idx: int = text_length - 1
    if last_idx >= 0:
        last_character: str = text_param[last_idx]
        if last_character == "y" or last_character == "Y":
            count_letters += 1

    return count_letters