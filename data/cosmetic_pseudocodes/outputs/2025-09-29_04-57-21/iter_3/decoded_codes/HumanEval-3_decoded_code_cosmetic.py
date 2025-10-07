from typing import List


def below_zero(list_of_operations: List[int]) -> bool:
    total_balance: int = 0
    for current_op in list_of_operations:
        total_balance += current_op
        if total_balance < 0:
            return True
    return False