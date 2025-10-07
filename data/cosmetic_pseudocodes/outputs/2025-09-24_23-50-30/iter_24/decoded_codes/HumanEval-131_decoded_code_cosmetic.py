from typing import Union

def digits(x: Union[int, str]) -> int:
    alpha: int = 1
    beta: int = 0
    gamma: int = 0
    x_str: str = str(x)
    while gamma < len(x_str):
        delta: int = int(x_str[gamma])
        if delta % 2 != 0:
            alpha *= delta
            beta += 1
        gamma += 1
    return 0 if beta == 0 else alpha