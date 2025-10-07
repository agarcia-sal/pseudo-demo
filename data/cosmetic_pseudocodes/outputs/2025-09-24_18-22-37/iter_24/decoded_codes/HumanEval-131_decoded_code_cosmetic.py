from typing import Union


def digits(n: int) -> int:
    result_product: int = 1
    counter_odd: int = 0
    str_n: str = str(n)
    index_i: int = 0
    while index_i < len(str_n):
        char_c: str = str_n[index_i]
        num_val: int = int(char_c)
        if num_val % 2 == 1:
            result_product *= num_val
            counter_odd += 1
        index_i += 1
    flag_no_odds: bool = (counter_odd == 0)
    if flag_no_odds:
        return 0
    else:
        return result_product