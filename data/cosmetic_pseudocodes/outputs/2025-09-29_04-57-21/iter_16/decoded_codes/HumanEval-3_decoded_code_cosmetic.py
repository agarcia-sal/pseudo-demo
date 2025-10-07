from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    balanceCounter: int = 0
    iterator = iter(list_of_operations)

    for currentOperation in iterator:
        balanceCounter += currentOperation
        if balanceCounter < 0:
            return True

    return False