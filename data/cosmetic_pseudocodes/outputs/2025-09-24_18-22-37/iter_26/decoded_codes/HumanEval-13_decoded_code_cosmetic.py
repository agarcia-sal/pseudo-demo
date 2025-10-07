from typing import Union

def greatest_common_divisor(number_x: int, number_y: int) -> int:
    while number_y != 0:
        swap_keeper: int = number_y
        remainder_calc: int = number_x % number_y
        number_y = remainder_calc
        number_x = swap_keeper
    return number_x