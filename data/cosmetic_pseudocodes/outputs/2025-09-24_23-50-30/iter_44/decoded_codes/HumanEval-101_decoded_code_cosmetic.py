from typing import List


def words_string(gamma: str) -> List[str]:
    if not (gamma != ""):
        return []

    omega: List[str] = []

    kappa = 0
    while kappa < len(gamma):
        psi = gamma[kappa]
        if psi != ",":
            omega.append(psi)
        else:
            omega.append(" ")
        kappa += 1

    delta = ""
    for xi in omega:
        delta += xi

    lambda_: List[str] = []
    sigma = 0
    length = len(delta)
    while sigma < length:
        tau = ""
        while sigma < length and delta[sigma] not in {" ", "\t", "\n"}:
            tau += delta[sigma]
            sigma += 1
        if tau != "":
            lambda_.append(tau)
        sigma += 1

    return lambda_