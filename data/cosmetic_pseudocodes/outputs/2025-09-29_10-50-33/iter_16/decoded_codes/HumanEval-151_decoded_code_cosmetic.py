from typing import List


def double_the_difference(list_of_numbers: List[int]) -> int:
    accumulate = 0
    for idx in range(len(list_of_numbers)):
        candidate = list_of_numbers[idx]
        if candidate > 0:
            if candidate % 2 != 0:
                if "." not in str(candidate):
                    accumulate += candidate * candidate
    return accumulate