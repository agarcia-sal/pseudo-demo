from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    total: int = 0

    def iter(ops: List[int]) -> bool:
        nonlocal total
        if not ops:
            return False
        head, tail = ops[0], ops[1:]
        total += head
        if total < 0:
            return True
        return iter(tail)

    return iter(list_of_operations)