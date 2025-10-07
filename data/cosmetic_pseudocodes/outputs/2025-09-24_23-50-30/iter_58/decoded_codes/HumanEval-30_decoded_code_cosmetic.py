from typing import List

def get_positive(lambda_omega: List[float]) -> List[float]:
    theta_sigma: List[float] = []
    pi_kappa: int = 0
    while pi_kappa < len(lambda_omega):
        if lambda_omega[pi_kappa] > 0:
            theta_sigma.append(lambda_omega[pi_kappa])
        pi_kappa += 1
    return theta_sigma