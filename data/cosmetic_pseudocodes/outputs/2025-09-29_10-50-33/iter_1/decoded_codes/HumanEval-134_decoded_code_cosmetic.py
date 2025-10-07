from typing import List


def check_if_last_char_is_a_letter(text: str) -> bool:
    words_list: List[str] = text.split(" ")
    if not words_list:
        return False
    last_token: str = words_list[-1]
    if len(last_token) == 1:
        ch: str = last_token.lower()
        ascii_val: int = ord(ch)
        if 97 <= ascii_val <= 122:
            return True
    return False