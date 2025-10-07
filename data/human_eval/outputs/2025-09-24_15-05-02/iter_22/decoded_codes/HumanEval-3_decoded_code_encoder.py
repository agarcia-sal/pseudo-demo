from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    account_balance: int = 0
    for operation in list_of_operations:
        account_balance += operation
        if account_balance < 0:
            return True
    return False