from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    def check(idx: int, accum: int) -> bool:
        if idx == len(list_of_operations):
            return False
        new_accum = accum + list_of_operations[idx]
        return new_accum < 0 or check(idx + 1, new_accum)
    return check(0, 0)