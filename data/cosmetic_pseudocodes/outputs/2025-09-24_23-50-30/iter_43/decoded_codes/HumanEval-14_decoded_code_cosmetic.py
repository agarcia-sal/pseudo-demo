from typing import List

def all_prefixes(gamma: str) -> List[str]:
    theta: List[str] = []
    kappa: int = 0
    while kappa < len(gamma):
        lambda_: str = gamma[:kappa + 1]  # prefix from start to kappa inclusive
        theta.append(lambda_)
        kappa += 1
    return theta