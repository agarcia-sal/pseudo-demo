from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def helper_contains_zero(lst: List[int], idx: int) -> bool:
        if idx == len(lst):
            return False
        return lst[idx] == 0 or helper_contains_zero(lst, idx + 1)

    def helper_count_negatives(lst: List[int], idx: int, acc: int) -> int:
        if idx == len(lst):
            return acc
        return helper_count_negatives(lst, idx + 1, acc + (1 if lst[idx] < 0 else 0))

    def helper_sum_abs(lst: List[int], idx: int, acc: int) -> int:
        if idx == len(lst):
            return acc
        return helper_sum_abs(lst, idx + 1, acc + abs(lst[idx]))

    if len(array_of_integers) == 0:
        return None

    if helper_contains_zero(array_of_integers, 0):
        sign_accumulator = 0
    else:
        negative_count = helper_count_negatives(array_of_integers, 0, 0)
        sign_accumulator = (-1) ** negative_count

    magnitude_sum = helper_sum_abs(array_of_integers, 0, 0)
    return sign_accumulator * magnitude_sum