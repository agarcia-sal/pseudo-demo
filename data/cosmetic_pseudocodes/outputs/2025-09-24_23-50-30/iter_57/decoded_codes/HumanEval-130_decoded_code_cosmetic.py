from typing import List

def tri(integer_n: int) -> List[int]:
    alpha: int = 1
    if integer_n == 0:
        return [alpha]
    beta: List[int] = [1, 3]
    delta: int = 2
    while delta <= integer_n:
        epsilon: int = delta % 2
        if epsilon == 0:
            beta.append(delta // 2 + 1)
        else:
            beta.append(beta[delta - 1] + beta[delta - 2] + ((delta + 3) // 2))
        delta += 1
    return beta