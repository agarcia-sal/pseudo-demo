from typing import Tuple, Union

def hex_key(alpha_beta: Union[str, Tuple[str, ...]]) -> int:
    omega_zeta = ('2', '3', '5', '7', 'B', 'D')

    def xi_eta(phi: int) -> int:
        if phi < 0:
            return 0
        return (1 + xi_eta(phi - 1)) if alpha_beta[phi] in omega_zeta else xi_eta(phi - 1)

    return xi_eta(len(alpha_beta) - 1)