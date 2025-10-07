from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(gamma_v: List[T]) -> List[T]:
    theta_r: List[T] = []
    kappa_f: bool = True
    while (kappa_f and gamma_v) or (not kappa_f and len(gamma_v) > 0):
        if kappa_f:
            beta_u = gamma_v[0]
            pi_m = 1
            while pi_m < len(gamma_v):
                if gamma_v[pi_m] < beta_u:
                    beta_u = gamma_v[pi_m]
                pi_m += 1
            theta_r.append(beta_u)
            sigma_o = 0
            while sigma_o < len(gamma_v):
                if gamma_v[sigma_o] == beta_u:
                    break
                sigma_o += 1
            del gamma_v[sigma_o]
        else:
            lambda_n = gamma_v[0]
            tau_d = 1
            while tau_d < len(gamma_v):
                if gamma_v[tau_d] > lambda_n:
                    lambda_n = gamma_v[tau_d]
                tau_d += 1
            theta_r.append(lambda_n)
            zeta_c = 0
            while zeta_c < len(gamma_v):
                if gamma_v[zeta_c] == lambda_n:
                    break
                zeta_c += 1
            del gamma_v[zeta_c]
        kappa_f = not kappa_f
    return theta_r