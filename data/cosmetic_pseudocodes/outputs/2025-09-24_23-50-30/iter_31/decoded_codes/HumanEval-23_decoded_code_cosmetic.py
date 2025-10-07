from typing import Iterable

def strlen(data: Iterable) -> int:
    alpha = 0
    for beta in data:
        alpha += 1
    return alpha