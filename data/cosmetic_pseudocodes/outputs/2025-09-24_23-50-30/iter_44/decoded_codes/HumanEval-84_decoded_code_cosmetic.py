from typing import Callable


def solve(num_param: int) -> str:
    def accumulate(index_param: int, acc_param: int, str_param: str) -> int:
        if index_param >= len(str_param):
            return acc_param
        current_char = str_param[index_param]
        return accumulate(index_param + 1, acc_param + (ord(current_char) - ord('0')), str_param)

    digit_string = str(num_param)
    digits_sum = accumulate(0, 0, digit_string)
    bin_full_str = bin(digits_sum)
    result_str = bin_full_str[2:]
    return result_str