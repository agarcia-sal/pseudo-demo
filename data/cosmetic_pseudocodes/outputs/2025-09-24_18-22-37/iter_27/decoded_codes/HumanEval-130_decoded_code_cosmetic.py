from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]
    alpha: List[int] = [1, 3]
    beta_index: int = 2
    while beta_index <= integer_n:
        gamma: int = beta_index % 2
        if gamma == 0:
            delta: int = beta_index // 2
            epsilon: int = delta + 1
            alpha.append(epsilon)
        else:
            zeta: int = beta_index - 1
            eta: int = beta_index - 2
            theta: int = beta_index + 3
            iota: int = theta // 2
            kappa: int = alpha[zeta]
            lambda_: int = alpha[eta]
            mu: int = kappa + lambda_ + iota
            alpha.append(mu)
        beta_index += 1
    return alpha