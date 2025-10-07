from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def helper(index: int, current_balance: int) -> bool:
        if index == len(list_of_operations):
            return False
        updated_balance = current_balance + list_of_operations[index]
        if updated_balance < 0:
            return True
        return helper(index + 1, updated_balance)
    return helper(0, 0)