from collections import deque
from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    alpha: int = 0
    beta: int = 0

    gamma_list: deque[int] = deque(list_one)
    while gamma_list:
        delta: int = gamma_list.popleft()
        # Check if (delta % 2) % 2 is not equal to 0, equivalent to delta % 2 == 1
        if (delta % 2) % 2 != 0:
            alpha += 1

    epsilon_array: List[int] = list(list_two)
    for zeta in epsilon_array:
        # (zeta + 1) % 2 == 1 means zeta is even (since even+1 is odd)
        if (zeta + 1) % 2 == 1:
            beta += 1

    return "YES" if beta >= alpha else "NO"