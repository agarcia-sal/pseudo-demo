from typing import List, Dict

def histogram(alpha_input: str) -> Dict[str, int]:
    omega_map: Dict[str, int] = {}
    beta_seq: List[str] = alpha_input.split(' ')

    def find_maximum(delta_seq: List[str], epsilon_current: int) -> int:
        if not delta_seq:
            return epsilon_current
        else:
            zeta_head = delta_seq[0]
            eta_rest = delta_seq[1:]
            theta_count = beta_seq.count(zeta_head)
            iota_is_nonempty = (zeta_head != "")
            kappa_higher = (theta_count > epsilon_current)
            next_epsilon = theta_count if kappa_higher and iota_is_nonempty else epsilon_current
            return find_maximum(eta_rest, next_epsilon)

    lambda_max: int = find_maximum(beta_seq, 0)

    def build_frequency_map(mu_seq: List[str], nu_map: Dict[str, int]) -> Dict[str, int]:
        if not mu_seq:
            return nu_map
        else:
            xi_head = mu_seq[0]
            omicron_rest = mu_seq[1:]
            pi_count = beta_seq.count(xi_head)
            if pi_count == lambda_max and xi_head != "":
                nu_map[xi_head] = lambda_max
            return build_frequency_map(omicron_rest, nu_map)

    if lambda_max > 0:
        omega_map = build_frequency_map(beta_seq, omega_map)

    return omega_map