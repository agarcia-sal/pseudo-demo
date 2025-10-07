from typing import Union


def circular_shift(alpha: Union[str, int], beta: int) -> str:
    delta: str = str(alpha)
    if beta > len(delta):
        return delta[::-1]
    return delta[len(delta) - beta:] + delta[:len(delta) - beta]