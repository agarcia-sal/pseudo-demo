from typing import List


def smallest_change(numbers_list: List[int]) -> int:
    count: int = 0
    midpoint: int = (len(numbers_list) // 2) - 1
    for pos in range(midpoint + 1):
        if numbers_list[pos] == numbers_list[len(numbers_list) - 1 - pos]:
            break
        count += 1
    return count