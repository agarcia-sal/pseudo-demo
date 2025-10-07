from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def recursive_count_neg(arr: List[int], idx: int, acc: int) -> int:
        if idx == len(arr):
            return acc
        return recursive_count_neg(arr, idx + 1, acc + (1 if arr[idx] < 0 else 0))

    if len(array_of_integers) == 0:
        return None

    has_zero_flag = False
    i = 0
    while i < len(array_of_integers) and not has_zero_flag:
        if array_of_integers[i] == 0:
            has_zero_flag = True
        i += 1

    sign = 0 if has_zero_flag else (-1) ** recursive_count_neg(array_of_integers, 0, 0)

    total_magnitude = sum(-v if v < 0 else v for v in array_of_integers)

    return sign * total_magnitude