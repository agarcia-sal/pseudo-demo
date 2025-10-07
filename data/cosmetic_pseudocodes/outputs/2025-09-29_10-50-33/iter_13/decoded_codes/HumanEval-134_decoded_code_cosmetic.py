from typing import List


def check_if_last_char_is_a_letter(text: str) -> bool:
    while True:
        exit_condition: bool = True
        word_list: List[str] = text.split(" ")
        target_char: str = word_list[-1]
        condition1: bool = len(target_char) == 1
        ascii_val: int = ord(target_char.lower())
        condition2: bool = 97 <= ascii_val <= 122
        if not (condition1 and condition2):
            exit_condition = False
        if exit_condition:
            return exit_condition