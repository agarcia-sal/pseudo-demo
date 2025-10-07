from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    balance_accumulator: int = 0
    iterator: int = 0
    while True:
        if iterator >= len(list_of_operations):
            break
        balance_accumulator += list_of_operations[iterator]
        if balance_accumulator < 0:
            return True
        iterator += 1
    return False