from typing import List

def exchange(array_alpha: List[int], array_beta: List[int]) -> str:
    count_odd: int = 0
    count_even: int = 0
    for val_alpha in array_alpha:
        count_odd += 1 if val_alpha % 2 == 1 else 0
    for val_beta in array_beta:
        count_even += 1 if val_beta % 2 == 0 else 0
    if count_even >= count_odd:
        return "YES"
    return "NO"