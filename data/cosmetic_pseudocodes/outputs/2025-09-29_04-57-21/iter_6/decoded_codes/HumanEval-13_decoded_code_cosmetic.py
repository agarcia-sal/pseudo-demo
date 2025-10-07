from typing import Union

def greatest_common_divisor(a_num: int, b_num: int) -> int:
    while True:
        if b_num == 0:
            break
        swap_holder = b_num
        b_num = a_num - (a_num // b_num) * b_num
        a_num = swap_holder
    return a_num