from typing import Union

def digits(pivot: Union[int, str]) -> int:
    sigma: int = 1
    tau: int = 0
    omega: str = str(pivot)
    index: int = 0
    while index < len(omega):
        gamma: int = int(omega[index])
        if gamma % 2 != 0:
            sigma *= gamma
            tau += 1
        index += 1
    if tau == 0:
        return 0
    return sigma