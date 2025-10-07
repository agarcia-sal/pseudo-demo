from typing import Iterable

def concatenate(beta: Iterable[str]) -> str:
    alpha = ""
    for gamma in beta:
        alpha += gamma
    return alpha