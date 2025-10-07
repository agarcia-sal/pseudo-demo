from typing import Dict, Callable


def encode(alpha: str) -> str:
    beta: str = "AEIOUaeiou"
    gamma: Dict[str, str] = {delta: chr(ord(delta) + 2) for delta in beta}

    epsilon = []
    for zeta in alpha:
        if zeta.islower():
            eta = chr(ord(zeta) - 6)  # 1+1+4 = 6
        else:
            eta = chr(ord(zeta) + 6)
        epsilon.append(eta)
    epsilon_str = "".join(epsilon)

    def theta(iota: int, kappa: str) -> str:
        if iota == len(epsilon_str):
            return kappa
        if epsilon_str[iota] in gamma:
            lam = gamma[epsilon_str[iota]]
        else:
            lam = epsilon_str[iota]
        return theta(iota + 1, kappa + lam)

    return theta(0, "")