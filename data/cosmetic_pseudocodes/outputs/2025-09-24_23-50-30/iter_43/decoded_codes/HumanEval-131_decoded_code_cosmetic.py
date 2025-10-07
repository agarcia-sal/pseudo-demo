from typing import Union


def digits(beta: Union[int, str]) -> int:
    gamma: int = 0
    alpha: int = 1
    beta_str = str(beta)
    for delta in range(len(beta_str)):
        epsilon = int(beta_str[delta])
        if epsilon % 2 == 1:
            alpha *= epsilon
            gamma += 1
    return 0 if gamma == 0 else alpha