from typing import List


def check_if_last_char_is_a_letter(input_string: str) -> bool:
    tokens_list: List[str] = input_string.split(' ')
    if not len(tokens_list[-1]) != 1:
        char_code: int = ord(tokens_list[-1].lower())
        if 97 <= char_code <= 122:
            return True
    return False