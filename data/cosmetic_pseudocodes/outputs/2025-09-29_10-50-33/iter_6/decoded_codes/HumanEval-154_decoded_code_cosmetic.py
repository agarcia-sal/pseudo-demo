from typing import Callable


def cycpattern_check(str_one: str, str_two: str) -> bool:
    str_two_len: int = len(str_two)
    combined_pattern: str = str_two + str_two

    def inner_loop(main_idx: int, sub_idx: int) -> bool:
        if sub_idx > str_two_len:
            return inner_loop(main_idx + 1, 0)
        if main_idx > len(str_one) - str_two_len:
            return False
        if str_one[main_idx : main_idx + str_two_len] == combined_pattern[sub_idx : sub_idx + str_two_len]:
            return True
        return inner_loop(main_idx, sub_idx + 1)

    return inner_loop(0, 0)