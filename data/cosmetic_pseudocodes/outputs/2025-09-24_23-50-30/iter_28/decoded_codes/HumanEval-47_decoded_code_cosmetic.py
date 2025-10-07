from typing import List, Union

def median(alpha: List[Union[int, float]]) -> float:
    def omega(beta: List[Union[int, float]], delta: int, gamma: int) -> None:
        if delta < gamma:
            epsilon = beta[delta]
            zeta = delta
            for eta in range(delta + 1, gamma + 1):
                if beta[eta] < epsilon:
                    epsilon = beta[eta]
                    zeta = eta
            beta[zeta], beta[delta] = beta[delta], beta[zeta]
            omega(beta, delta + 1, gamma)

    iota = len(alpha)
    kappa = alpha.copy()
    if iota > 0:
        omega(kappa, 0, iota - 1)
        lambda_ = iota // 2
        if iota % 2 == 1:
            return float(kappa[lambda_])
        else:
            return (kappa[lambda_ - 1] + kappa[lambda_]) / 2.0
    else:
        raise ValueError("median() arg is an empty list")