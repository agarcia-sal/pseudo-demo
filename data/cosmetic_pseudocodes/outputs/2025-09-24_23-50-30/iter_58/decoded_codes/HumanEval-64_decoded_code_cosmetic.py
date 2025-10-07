from typing import Union


def vowels_count(beta: str) -> int:
    gamma: str = "aeiouAEIOU"
    delta: int = 0
    for epsilon in beta:
        if epsilon in gamma:
            delta += 1  # increment delta by 1
    if beta and beta[-1] in {'y', 'Y'}:
        delta += 1
    return delta