from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    outer_index: int = 0
    limit: int = len(list_of_integers) - 1
    while outer_index <= limit:
        current_value: int = list_of_integers[outer_index]
        inner_index: int = outer_index + 1
        while True:
            if inner_index > limit:
                break
            next_value: int = list_of_integers[inner_index]
            total_sum: int = current_value + next_value
            if total_sum == 0:
                return True
            inner_index += 1
        outer_index += 1
    return False