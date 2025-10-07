from typing import List

def add(list_of_integers: List[int]) -> int:
    accumulator_result: int = 0
    current_idx: int = 1
    while current_idx < len(list_of_integers):
        candidate_val: int = list_of_integers[current_idx]
        if candidate_val % 2 == 0:
            accumulator_result += candidate_val
        current_idx += 2
    return accumulator_result