from typing import List

def is_nested(puzzle: str) -> bool:
    alpha: List[int] = []
    beta: List[int] = []
    for k in range(len(puzzle)):
        if puzzle[k] == '[':
            alpha.append(k)
        else:
            beta.append(k)
    gamma = len(beta)
    delta = 0
    epsilon = 0
    while epsilon < len(alpha):
        if delta < gamma and alpha[epsilon] < beta[delta]:
            delta += 1
            epsilon += 1
            continue
        else:
            epsilon += 1
    return delta >= 2