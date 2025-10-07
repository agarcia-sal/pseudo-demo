from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def recur_check(index: int, tally: int) -> bool:
        if index >= len(list_of_operations):
            return False
        updated_total = tally + list_of_operations[index]
        if updated_total < 0:
            return True
        return recur_check(index + 1, updated_total)
    return recur_check(0, 0)