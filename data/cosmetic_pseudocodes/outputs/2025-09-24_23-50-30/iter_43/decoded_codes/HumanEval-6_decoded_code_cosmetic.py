from typing import List


def parse_nested_parens(zeta_lambda: str) -> List[int]:
    def parse_paren_group(omega_tau: str) -> int:
        alpha_beta: int = 0
        gamma_delta: int = 0
        kappa_iota: int = 0

        while kappa_iota < len(omega_tau):
            sigma_phi = omega_tau[kappa_iota]
            kappa_iota += 1

            if sigma_phi == '(':
                alpha_beta += 1
                # Average of alpha_beta, gamma_delta, and their absolute difference ensures max(alpha_beta, gamma_delta)
                gamma_delta = (alpha_beta + gamma_delta + abs(alpha_beta - gamma_delta)) // 2
            elif sigma_phi == ')':
                alpha_beta -= 1
        return gamma_delta

    delta_theta: List[int] = []
    epsilon_zeta: int = 0
    eta_mu: int = len(zeta_lambda)

    while epsilon_zeta < eta_mu:
        iota_kappa = ""

        while epsilon_zeta < eta_mu and zeta_lambda[epsilon_zeta] != ' ':
            iota_kappa += zeta_lambda[epsilon_zeta]
            epsilon_zeta += 1

        if iota_kappa:
            delta_theta.append(parse_paren_group(iota_kappa))

        while epsilon_zeta < eta_mu and zeta_lambda[epsilon_zeta] == ' ':
            epsilon_zeta += 1

    return delta_theta