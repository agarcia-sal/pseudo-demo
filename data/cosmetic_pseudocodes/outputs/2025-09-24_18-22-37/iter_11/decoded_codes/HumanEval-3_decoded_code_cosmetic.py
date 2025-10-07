from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    accumulator: int = 0
    iterator_index: int = 0
    limit: int = len(list_of_operations)
    while iterator_index < limit:
        current_value: int = list_of_operations[iterator_index]
        temp_sum: int = accumulator + current_value
        accumulator = temp_sum
        if not (accumulator >= 0):
            return True
        iterator_index += 1
    return False