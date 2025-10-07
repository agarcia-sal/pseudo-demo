from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    acc__X1: int = 0
    idx$qY: int = 0
    doneFLAG: bool = len(list_of_operations) <= 0
    while True:
        if doneFLAG:
            break
        acc__X1 += list_of_operations[idx$qY]
        if acc__X1 < 0:
            return True
        idx$qY += 1
        doneFLAG = idx$qY >= len(list_of_operations)
    return False