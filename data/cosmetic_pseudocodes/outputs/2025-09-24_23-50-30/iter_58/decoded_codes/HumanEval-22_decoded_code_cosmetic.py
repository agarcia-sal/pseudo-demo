from typing import List, Union

def filter_integers(alpha: List[object]) -> List[int]:
    beta: List[int] = []
    gamma: int = 0

    while gamma < len(alpha):
        delta = alpha[gamma]

        if not isinstance(delta, int):
            gamma += 1
            continue
        else:
            beta.append(delta)

        gamma += 1

    return beta