from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    counter: int = 0
    index: int = 0
    while index < len(list_of_operations):
        counter += list_of_operations[index]
        if counter < 0:
            return True
        index += 1
    return False