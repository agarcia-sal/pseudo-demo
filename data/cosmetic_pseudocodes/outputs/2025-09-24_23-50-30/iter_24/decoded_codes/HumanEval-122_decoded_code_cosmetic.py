from typing import List

def add_elements(beta: List[int], gamma: int) -> int:
    delta: int = 0
    epsilon: int = 0
    while epsilon < gamma:
        if 2 >= len(str(beta[epsilon])):
            delta += beta[epsilon]
        epsilon += 1
    return delta