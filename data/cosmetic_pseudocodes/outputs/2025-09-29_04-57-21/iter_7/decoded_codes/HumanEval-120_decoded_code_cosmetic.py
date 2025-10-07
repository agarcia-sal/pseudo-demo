from typing import List


def maximum(numbers_list: List[int], count_positive: int) -> List[int]:
    if count_positive == 0:
        return []

    numbers_list.sort()
    return numbers_list[-count_positive:] if count_positive <= len(numbers_list) else numbers_list[:]