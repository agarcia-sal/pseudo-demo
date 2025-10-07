from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    total: int = 0
    idx: int = 0
    length: int = len(list_of_operations)
    while True:
        if idx >= length:
            break
        current_operation: int = list_of_operations[idx]
        total += current_operation
        if total < 0:
            return True
        idx += 1
    return False