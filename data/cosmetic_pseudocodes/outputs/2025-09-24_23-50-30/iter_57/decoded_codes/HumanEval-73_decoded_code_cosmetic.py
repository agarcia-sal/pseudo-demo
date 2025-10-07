from typing import List


def smallest_change(list_of_numbers: List[int]) -> int:
    result_accum: int = 0
    n: int = len(list_of_numbers)
    for iter_var in range(n // 2):
        if list_of_numbers[iter_var] != list_of_numbers[n - 1 - iter_var]:
            result_accum += 1
    return result_accum