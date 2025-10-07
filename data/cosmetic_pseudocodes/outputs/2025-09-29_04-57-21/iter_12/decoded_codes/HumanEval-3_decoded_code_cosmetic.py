from typing import Sequence

def below_zero(list_of_operations: Sequence[int]) -> bool:
    cumulative_sum = 0
    current_index = 0
    while current_index < len(list_of_operations):
        current_operation = list_of_operations[current_index]
        cumulative_sum += current_operation
        if cumulative_sum < 0:
            return True
        current_index += 1
    return False