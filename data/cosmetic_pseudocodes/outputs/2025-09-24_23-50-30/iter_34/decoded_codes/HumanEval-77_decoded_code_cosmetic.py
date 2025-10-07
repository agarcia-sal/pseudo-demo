from typing import Union

def iscube(beta: Union[int, float]) -> bool:
    gamma = round(abs(beta) ** (1 / 3))
    delta = gamma ** 3
    return delta == abs(beta)