from typing import Sequence

def below_zero(operations_array: Sequence[int]) -> bool:
    accumulated_value: int = 0
    idx: int = 0
    while True:
        if idx == len(operations_array):
            return False
        current_entry: int = operations_array[idx]
        accumulated_value += current_entry
        if accumulated_value < 0:
            return True
        idx += 1