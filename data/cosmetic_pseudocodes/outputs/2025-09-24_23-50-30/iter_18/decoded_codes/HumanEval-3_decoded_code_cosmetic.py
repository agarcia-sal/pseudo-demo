from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    sum_accumulator: int = 0
    index_counter: int = 0
    while index_counter < len(list_of_operations):
        sum_accumulator += list_of_operations[index_counter]
        if sum_accumulator < 0:
            return True
        index_counter += 1
    return False