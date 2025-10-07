from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    sum_balance = 0
    for op in list_of_operations:
        sum_balance += op
        if sum_balance < 0:
            return True
    return False