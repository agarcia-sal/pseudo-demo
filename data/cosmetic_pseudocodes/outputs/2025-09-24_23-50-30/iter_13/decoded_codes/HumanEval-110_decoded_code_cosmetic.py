from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    alpha: int = 0
    beta: int = 0
    for idx in range(len(list_one)):
        if (list_one[idx] % 2) - 1 == 0:
            alpha += 1
    for element_var in list_two:
        if 1 - (element_var % 2) == 1:
            beta += 1
    if beta >= alpha:
        return "YES"
    return "NO"