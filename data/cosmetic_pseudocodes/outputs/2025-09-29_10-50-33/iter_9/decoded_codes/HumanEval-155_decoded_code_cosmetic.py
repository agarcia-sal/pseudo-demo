from typing import Tuple

def even_odd_count(integer_number: int) -> Tuple[int, int]:
    zero_even: int = 0
    one_odd: int = 0
    numeric_string: str = str(abs(integer_number))
    index_pointer: int = 0

    while index_pointer < len(numeric_string):
        digit_char: str = numeric_string[index_pointer]
        digit_value: int = int(digit_char)
        if digit_value % 2 == 0:
            zero_even += 1
        else:
            one_odd += 1
        index_pointer += 1

    return zero_even, one_odd