from typing import Tuple

def even_odd_count(integer_number: int) -> Tuple[int, int]:
    def counter(accumulator: Tuple[int, int], index: int) -> Tuple[int, int]:
        str_num = str(abs(integer_number))
        if index >= len(str_num):
            return accumulator
        digit_value = int(str_num[index])
        is_even = (digit_value % 2) == 0
        add_even = 1 if is_even else 0
        add_odd = 1 if not is_even else 0
        next_accumulator = (accumulator[0] + add_even, accumulator[1] + add_odd)
        return counter(next_accumulator, index + 1)
    return counter((0, 0), 0)