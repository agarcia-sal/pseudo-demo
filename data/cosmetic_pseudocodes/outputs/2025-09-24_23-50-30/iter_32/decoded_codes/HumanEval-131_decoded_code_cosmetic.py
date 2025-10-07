from typing import Union

def digits(x: Union[int, str]) -> int:
    alpha = 1
    beta = 0
    x_str = str(x)
    for gamma in range(len(x_str)):
        delta = int(x_str[gamma])
        if delta % 2 != 0:
            alpha *= delta
            beta += 1
    return alpha if beta != 0 else 0