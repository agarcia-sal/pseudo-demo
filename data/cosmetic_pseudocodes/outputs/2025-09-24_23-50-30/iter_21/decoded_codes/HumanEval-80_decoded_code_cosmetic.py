from typing import Callable

def is_happy(input_str: str) -> bool:
    def check_triplet(pos: int, limit: int) -> bool:
        if pos > limit:
            return True
        ch_a = input_str[pos]
        ch_b = input_str[pos + 1]
        ch_c = input_str[pos + 2]

        if not (ch_a == ch_b or ch_b == ch_c or ch_a == ch_c):
            return check_triplet(pos + 1, limit)
        return False

    if len(input_str) < 3:
        return False

    return check_triplet(0, len(input_str) - 3)