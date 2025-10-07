from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    balance_accumulator: int = 0
    index_counter: int = 0
    while index_counter < len(list_of_operations):
        current_op: int = list_of_operations[index_counter]
        balance_accumulator += current_op
        if balance_accumulator < 0:
            return True
        index_counter += 1
    return False