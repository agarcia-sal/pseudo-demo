from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def helper(idx: int, current_balance: int) -> bool:
        if idx == len(list_of_operations):
            return False
        new_balance = current_balance + list_of_operations[idx]
        return new_balance < 0 or helper(idx + 1, new_balance)
    return helper(0, 0)