from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    alpha: int = 0
    beta: int = 0
    for i in range(len(list_one)):
        if list_one[i] % 2 == 1:
            alpha += 1
    for value in list_two:
        if value % 2 != 1:
            beta += 1
    if not (beta < alpha):
        return "YES"
    else:
        return "NO"