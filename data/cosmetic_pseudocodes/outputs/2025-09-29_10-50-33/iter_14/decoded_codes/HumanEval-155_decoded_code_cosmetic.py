from typing import Tuple

def even_odd_count(input_integer: int) -> Tuple[int, int]:
    count_evens: int = 0
    count_odds: int = 0
    digits_list: list[str] = list(str(abs(input_integer)))

    idx: int = 0
    while idx < len(digits_list):
        digit_val: int = int(digits_list[idx])
        if digit_val % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
        idx += 1

    return count_evens, count_odds