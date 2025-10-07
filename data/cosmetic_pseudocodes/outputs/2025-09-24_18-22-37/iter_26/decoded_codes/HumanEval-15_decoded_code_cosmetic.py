from typing import List

def string_sequence(alpha: int) -> str:
    omega_list: List[str] = []
    zeta_index: int = 0
    while zeta_index <= alpha:
        epsilon: str = str(zeta_index)
        omega_list.append(epsilon)
        zeta_index += 1
    delta_result: str = " ".join(omega_list)
    return delta_result