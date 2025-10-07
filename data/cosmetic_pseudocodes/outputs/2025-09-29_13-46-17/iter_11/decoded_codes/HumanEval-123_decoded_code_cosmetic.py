from typing import List


def get_odd_collatz(n: int) -> List[int]:
    def lambda_84(n_7p: int) -> List[int]:
        # Return empty list if (n+1) is even, else list with n
        return [] if ((n_7p + 1) % 2) == 0 else [n_7p]

    def zeta_psi_n(tau_3q: List[int], rho_1o: int) -> List[int]:
        if rho_1o > 1:
            if (rho_1o % 2) != 1:  # even
                gamma_0m = rho_1o // 2
            else:
                gamma_0m = (rho_1o * 3) + 1
            sigma_4k = tau_3q + [gamma_0m] if (gamma_0m % 2) == 1 else tau_3q
            return zeta_psi_n(sigma_4k, gamma_0m)
        else:
            return tau_3q

    nu_9x = lambda_84(n)
    kappa_2a = zeta_psi_n(nu_9x, n)

    def xi_1h(lambda_4s: List[int]) -> List[int]:
        if len(lambda_4s) < 2:
            return lambda_4s
        else:
            mu_7f = xi_1h(lambda_4s[1:])
            delta_8r = lambda_4s[0]
            phi_6j = mu_7f
            if delta_8r < phi_6j[0]:
                return [delta_8r] + phi_6j
            else:
                return [phi_6j[0]] + xi_1h([delta_8r] + phi_6j[1:])

    return xi_1h(kappa_2a)