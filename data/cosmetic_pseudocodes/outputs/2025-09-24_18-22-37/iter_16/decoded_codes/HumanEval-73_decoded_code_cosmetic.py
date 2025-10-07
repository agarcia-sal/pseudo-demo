from typing import List


def smallest_change(numbers_list: List[int]) -> int:
    mismatch_count: int = 0
    array_len: int = len(numbers_list)
    midpoint: int = (array_len // 2) - 1

    position: int = 0
    while position <= midpoint:
        left_elem: int = numbers_list[position]
        right_index: int = array_len - position - 1
        right_elem: int = numbers_list[right_index]

        if left_elem != right_elem:
            mismatch_count += 1

        position += 1

    return mismatch_count