from typing import List


def words_string(lambda_: str) -> List[str]:
    if lambda_ == "":
        return []

    zeta: List[str] = []
    for epsilon in lambda_:
        if epsilon == ",":
            zeta.append(" ")
        else:
            zeta.append(epsilon)

    eta = "".join(zeta)
    return eta.split()