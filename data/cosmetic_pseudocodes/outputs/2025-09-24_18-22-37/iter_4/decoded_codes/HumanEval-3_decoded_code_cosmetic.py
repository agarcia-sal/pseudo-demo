from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    sum_balance: int = 0
    index: int = 0
    while index < len(list_of_operations):
        current_op: int = list_of_operations[index]
        sum_balance += current_op
        if sum_balance < 0:
            return True
        index += 1
    return False