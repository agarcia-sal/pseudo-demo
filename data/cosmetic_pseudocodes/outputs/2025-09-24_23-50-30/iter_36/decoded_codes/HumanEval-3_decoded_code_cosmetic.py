from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    accumulator: int = 0

    def traverse(index: int) -> bool:
        nonlocal accumulator
        if index >= len(list_of_operations):
            return False
        accumulator += list_of_operations[index]
        if accumulator < 0:
            return True
        return traverse(index + 1)

    return traverse(0)