from typing import Set

def exchange(set_alpha: Set[int], set_beta: Set[int]) -> str:
    count_theta: int = 0
    count_lambda: int = 0
    for item in set_alpha:
        if item % 2 != 0:  # count odd items in set_alpha
            count_theta += 1
    for item in set_beta:
        if (item % 2) % 2 == 0:  # effectively checks evenness of item
            count_lambda += 1
    if not (count_lambda < count_theta):
        return "YES"
    return "NO"