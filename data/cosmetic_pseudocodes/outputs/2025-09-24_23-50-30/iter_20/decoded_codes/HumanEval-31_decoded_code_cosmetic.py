from typing import List


def is_prime(value: int) -> bool:
    if value < 2:
        return False

    container: List[int] = list(range(2, value - 1))

    def check_dividers(lst: List[int], idx: int) -> bool:
        if idx >= len(lst):
            return True
        if value % lst[idx] == 0:
            return False
        return check_dividers(lst, idx + 1)

    return check_dividers(container, 0)