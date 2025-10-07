from typing import List

def f(delta_a: int) -> List[int]:
    omega: List[int] = []
    kappa: int = 1

    while kappa <= delta_a:
        if kappa % 2 != 1:
            theta: int = 1
            lambda_var: int = 1
            while lambda_var <= kappa:
                theta *= lambda_var
                lambda_var += 1
            mu: int = theta
            omega.append(mu)
        else:
            sigma: int = 0
            epsilon: int = 1
            while True:
                if epsilon > kappa:
                    break
                sigma += epsilon
                epsilon += 1
            nu: int = sigma
            omega.append(nu)
        kappa += 1

    return omega