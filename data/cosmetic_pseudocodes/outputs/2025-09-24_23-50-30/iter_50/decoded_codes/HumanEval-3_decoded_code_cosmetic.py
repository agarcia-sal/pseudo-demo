from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def helper(index: int, acc: int) -> bool:
        if not (index < len(list_of_operations)):
            return False
        updated_value = acc + list_of_operations[index]
        if updated_value < 0:
            return True
        return helper(index + 1, updated_value)
    return helper(0, 0)