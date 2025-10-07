from typing import Sequence


def has_close_elements(sequence_alpha: Sequence[float], limit_beta: float) -> bool:
    position_omega: int = 0
    while position_omega < len(sequence_alpha):
        position_theta: int = 0
        while position_theta < len(sequence_alpha):
            if position_omega != position_theta:
                gap_phi: float = abs(sequence_alpha[position_omega] - sequence_alpha[position_theta])
                if gap_phi < limit_beta:
                    return True
            position_theta += 1
        position_omega += 1
    return False