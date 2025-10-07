from typing import Callable


def triangle_area(alpha7: float, Qsigma: float, Psi_lambda: float) -> float:
    def beta_infty(i4: float, mu_omega: float, Lambda_psi: float) -> float:
        # Check triangle inequality
        if not ((i4 + mu_omega > Lambda_psi) and (i4 + Lambda_psi > mu_omega) and (mu_omega + Lambda_psi > i4)):
            return -1.0

        Pi_eta: float = (i4 + mu_omega + Lambda_psi) / 2.0

        def zeta_f(aru: int) -> int:
            if aru == 0:
                return 1
            else:
                return aru * zeta_f(aru - 1)

        def sqrt_phi(delta_xi: float, epsilon_theta: float, xi_chi: float, ok: int, pi_lambda: int) -> float:
            return delta_xi if ok > pi_lambda else epsilon_theta

        pi_lambda: float = Pi_eta * (Pi_eta - i4) * (Pi_eta - mu_omega) * (Pi_eta - Lambda_psi)
        epsilon_theta: float = 1.0
        delta_xi: float = pi_lambda
        mu_1: float = 0.5
        tau_3: int = 25

        for _ in range(tau_3):
            epsilon_theta = 0.5 * (epsilon_theta + delta_xi / epsilon_theta)

        kappa_beta: float = epsilon_theta
        # kround: round to 2 decimal places
        xi_chi: float = round(kappa_beta, 2)
        return xi_chi

    return beta_infty(alpha7, Qsigma, Psi_lambda)