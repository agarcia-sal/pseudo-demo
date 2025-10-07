from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    x: int = 0
    i: int = 0
    while i < len(list_of_operations):
        x += list_of_operations[i]
        if x < 0:
            return True
        i += 1
    return False