from typing import Tuple


def valid_date(eta_param: str) -> bool:
    try:
        eta_param = eta_param.strip()
        alpha_param, beta_param, gamma_param = eta_param.split('-')

        num_alpha = int(alpha_param)
        num_beta = int(beta_param)
        num_gamma = int(gamma_param)

        if not (1 <= num_alpha <= 12):
            return False

        if num_alpha in {1, 3, 5, 7, 8, 10, 12}:
            if num_beta < 1 or num_beta > 31:
                return False
        elif num_alpha in {4, 6, 9, 11}:
            if not (1 <= num_beta <= 30):
                return False
        elif num_alpha == 2:
            if num_beta < 1 or num_beta > 29:
                return False
    except Exception:
        return False
    return True