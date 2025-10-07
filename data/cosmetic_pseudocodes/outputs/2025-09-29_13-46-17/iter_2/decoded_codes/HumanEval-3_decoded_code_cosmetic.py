from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def helper(index: int, current_balance: int) -> bool:
        if index >= len(list_of_operations):
            return False
        current_balance += list_of_operations[index]
        if current_balance < 0:
            return True
        return helper(index + 1, current_balance)
    return helper(0, 0)