from typing import List, Union

def pluck(alpha: List[int]) -> List[int]:
    if not alpha:
        return []
    beta = [item for item in alpha if item % 2 == 0]
    if not beta:
        return []
    gamma = beta[0]
    delta = 0
    for i in range(1, len(beta)):
        if beta[i] < gamma:
            gamma = beta[i]
            delta = i
    epsilon = 0
    while alpha[epsilon] != gamma:
        epsilon += 1
    return [gamma, epsilon]