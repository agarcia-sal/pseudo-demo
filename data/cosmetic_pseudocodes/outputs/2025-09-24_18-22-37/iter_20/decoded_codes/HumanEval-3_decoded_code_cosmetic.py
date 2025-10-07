from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    accumulator: int = 0
    position: int = 0
    while position < len(list_of_operations):
        current_value: int = list_of_operations[position]
        temp_sum: int = accumulator + current_value
        accumulator = temp_sum
        if accumulator < 0:
            return True
        position += 1
    return False