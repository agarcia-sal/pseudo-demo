from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def recur(index: int, total: int) -> bool:
        if index >= len(list_of_operations):
            return False
        new_total = total + list_of_operations[index]
        if new_total < 0:
            return True
        return recur(index + 1, new_total)

    return recur(1, 0)