from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    alpha: int = 0
    beta: int = 0
    idx_one: int = 1
    while idx_one <= len(list_one):
        val_one = list_one[idx_one - 1]  # adjusting for 1-based index in pseudocode
        if val_one % 2 != 0:
            alpha += 1
        idx_one += 1

    idx_two: int = 1
    while idx_two <= len(list_two):
        val_two = list_two[idx_two - 1]  # adjusting for 1-based index in pseudocode
        if val_two % 2 == 0:
            beta += 1
        idx_two += 1

    if (beta - alpha) >= 0:
        return "YES"
    else:
        return "NO"