from typing import List, Dict

def by_length(omega: List[int]) -> List[str]:
    theta: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    sigma: List[int] = sorted(omega, reverse=True)
    lambda_: List[str] = []

    kappa: int = 0
    while kappa < len(sigma):
        rho: int = sigma[kappa]

        if rho in theta:
            lambda_.append(theta[rho])
        kappa += 1

    return lambda_