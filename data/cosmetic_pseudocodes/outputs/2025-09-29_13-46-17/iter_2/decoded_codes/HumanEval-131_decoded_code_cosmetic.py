from typing import Literal

def digits(n: int) -> int:
    def helper(str_num: str, odd_counter: int, prod: int) -> int:
        if not str_num:
            return 0 if odd_counter == 0 else prod
        current_char, rest_chars = str_num[0], str_num[1:]
        digit_val = int(current_char)
        if digit_val % 2 != 0:
            return helper(rest_chars, odd_counter + 1, prod * digit_val)
        else:
            return helper(rest_chars, odd_counter, prod)
    return helper(str(n), 0, 1)