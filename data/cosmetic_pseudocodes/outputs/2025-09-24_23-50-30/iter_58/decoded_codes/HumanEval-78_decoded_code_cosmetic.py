from typing import Sequence

def hex_key(beta: Sequence[str]) -> int:
    alpha = ('2', '3', '5', '7', 'B', 'D')
    gamma = 0
    delta = 0
    while delta < len(beta):
        if beta[delta] in alpha:
            gamma += 1
        delta += 1
    return gamma