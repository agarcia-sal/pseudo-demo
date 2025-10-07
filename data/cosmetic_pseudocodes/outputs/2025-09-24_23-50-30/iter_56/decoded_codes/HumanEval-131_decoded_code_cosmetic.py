from typing import Union


def digits(kappa: Union[int, str]) -> int:
    omega: int = 1
    delta: int = 0
    lambda_index: int = 0
    sigma_str: str = str(kappa)

    while lambda_index < len(sigma_str):
        gamma_char: str = sigma_str[lambda_index]
        zeta_val: int = int(gamma_char)
        if zeta_val % 2 == 1:
            omega *= zeta_val
            delta += 1
        # no operation if even
        lambda_index += 1

    return 0 if delta == 0 else omega