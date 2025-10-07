from typing import Iterable, List, Union


def filter_integers(alpha: Iterable[object]) -> List[int]:
    beta: List[int] = []
    for gamma in alpha:
        if not isinstance(gamma, int):
            continue
        beta.append(gamma)
    return beta