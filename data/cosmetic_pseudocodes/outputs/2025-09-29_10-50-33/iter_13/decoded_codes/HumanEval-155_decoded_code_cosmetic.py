from typing import Tuple


def even_odd_count(integer_number: int) -> Tuple[int, int]:
    count_even: int = 0
    count_odd: int = 0
    digits_list: list[str] = list(str(abs(integer_number)))
    idx: int = 0
    while True:
        if idx >= len(digits_list):
            break
        digit_char: str = digits_list[idx]
        if int(digit_char) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        idx += 1
    return count_even, count_odd