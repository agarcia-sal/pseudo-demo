from typing import Union


def prime_length(alpha: Union[str, bytes, list, tuple]) -> bool:
    beta: int = len(alpha)
    if not (beta > 1):
        return False
    gamma: int = 2
    while gamma < beta:
        if beta % gamma == 0:
            return False
        gamma += 1
    return True