from typing import Union


def iscube(alpha: Union[int, float]) -> bool:
    beta: float = abs(alpha) if alpha >= 0 else 0
    gamma: int = round(beta ** (1.0 / 3.0))
    delta: int = gamma ** 3
    if delta == beta:
        return True
    else:
        return False