from typing import Sequence

def pairs_sum_to_zero(collection_of_numbers: Sequence[int]) -> bool:
    omega: int = 0
    delta: int = len(collection_of_numbers)
    beta: int = 1
    while omega < delta:
        gamma: int = collection_of_numbers[omega]
        kappa: int = beta
        while kappa < delta:
            if gamma + collection_of_numbers[kappa] == 0:
                return True
            kappa += 1
        omega += 1
        beta = omega + 1
    return False