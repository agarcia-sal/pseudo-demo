from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    accumulator: int = 0
    iterator_index: int = 0
    while iterator_index < len(list_of_operations):
        current_value: int = list_of_operations[iterator_index]
        accumulator += current_value
        if not (accumulator >= 0):
            return True
        iterator_index += 1
    return False