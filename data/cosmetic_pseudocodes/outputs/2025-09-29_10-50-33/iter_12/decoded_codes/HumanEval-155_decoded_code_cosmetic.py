from typing import List, Callable

def even_odd_count(integer_number: int) -> tuple[int, int]:
    def traverse_digits(accum_even: int, accum_odd: int, digit_list: List[str]) -> tuple[int, int]:
        if not digit_list:
            return accum_even, accum_odd
        head_digit, tail_digits = digit_list[0], digit_list[1:]
        if int(head_digit) % 2 == 0:
            return traverse_digits(accum_even + 1, accum_odd, tail_digits)
        else:
            return traverse_digits(accum_even, accum_odd + 1, tail_digits)

    absolute_string = str(abs(integer_number))
    return traverse_digits(0 + 0, 0 | 0, list(absolute_string))