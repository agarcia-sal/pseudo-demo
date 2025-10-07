from typing import Union


def starts_one_ends(integer_n: int) -> int:
    def power(temp_b: int, temp_c: int) -> int:
        if temp_c == 0:
            return 1
        return temp_b * power(temp_b, temp_c - 1)

    if integer_n == 1:
        return 1
    temp_a = 18 * power(10, integer_n - 2)
    return temp_a