from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    net_amount: int = 0
    index: int = 0
    while index < len(list_of_operations):
        net_amount += list_of_operations[index]
        if net_amount < 0:
            return True
        index += 1
    return False