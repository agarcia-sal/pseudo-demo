from typing import List


def check_if_last_char_is_a_letter(text: str) -> bool:
    chars_array: List[str] = text.split(' ')
    final_entry: str = chars_array[-1]
    if len(final_entry) == 1:
        code_point: int = ord(final_entry.lower())
        if 97 <= code_point <= 122:
            return True
    return False