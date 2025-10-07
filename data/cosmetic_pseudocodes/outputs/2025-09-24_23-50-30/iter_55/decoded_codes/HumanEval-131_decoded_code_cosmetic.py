from typing import Union

def digits(q: Union[int, str]) -> int:
    alpha: int = 0
    beta: int = 1
    q_str: str = str(q)
    while alpha < len(q_str):
        gamma: int = int(q_str[alpha])
        if gamma % 2 != 0:
            beta *= gamma
            alpha += 1
            continue
        alpha += 1
    return 0 if beta == 1 else beta