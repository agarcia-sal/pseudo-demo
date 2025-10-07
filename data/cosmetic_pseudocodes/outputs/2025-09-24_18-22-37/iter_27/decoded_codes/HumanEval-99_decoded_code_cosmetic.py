from math import floor, ceil
from typing import Union


def closest_integer(tau: Union[str, float]) -> int:
    # Initialize all variables as per pseudocode (though many are unused ultimately)
    phi: int = 0
    psi: int = 0

    chi: int = 0
    omega: int = 1
    sigma: int = 0
    upsilon: int = 0

    rho: int = 0

    eta: int = 0

    delta: int = 0
    gamma: int = 0
    theta: int = 0

    lambd: int = 0  # lambda is a reserved keyword; renamed locally

    mu: int = 0
    nu: int = 0
    xi: int = 0

    pi: int = 0

    alpha: int = 0
    beta: int = 0

    kappa: int = 0
    zeta: int = 0

    epsilon: int = 0
    iota: int = 0

    psi = 0

    num: float = 0.0

    tau_str: str = str(tau)

    tau_len: int = len(tau_str)

    count_dot: int = 0

    count_dot = 0
    lambd = 0

    while lambd < tau_len:
        if tau_str[lambd] == '.':
            count_dot += 1
        lambd += 1

    if count_dot == 1:
        alpha = len(tau_str)
        # Strip trailing zeros at the end of the string only if '.' is present
        while alpha > 1 and tau_str[alpha - 1] == '0':
            tau_str = tau_str[: alpha - 1]
            alpha -= 1

    num = float(tau_str)

    kappa = len(tau_str)

    circle: str = ""
    card: int = 0

    if kappa >= 2:
        circle = tau_str[kappa - 2 : kappa]
    else:
        circle = ""

    if circle == ".5":
        if num > 0:
            card = ceil(num)
        else:
            card = floor(num)
    else:
        if kappa > 0:
            card = round(num)
        else:
            card = 0

    return card