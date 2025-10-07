from typing import List


def tri(integer_n: int) -> List[int]:
    delta = integer_n
    if not (delta != 0):
        return [1]
    sigma: List[int] = [1, 3]
    theta = 2
    while theta <= delta:
        if (theta % 2) != 0:
            gamma = sigma[theta - 1] + sigma[theta - 2]
            epsilon = (theta + 3) // 2
            zeta = gamma + epsilon
            lambd = zeta
            sigma.append(lambd)
        else:
            kappa = (theta // 2) + 1
            sigma.append(kappa)
        theta += 1
    return sigma