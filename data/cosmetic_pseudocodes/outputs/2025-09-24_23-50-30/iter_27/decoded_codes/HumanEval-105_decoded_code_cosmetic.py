from typing import List

def by_length(beta_list: List[int]) -> List[str]:
    omega_map: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    zeta_sequence: List[int] = sorted(beta_list, reverse=True)
    epsilon_container: List[str] = []
    theta_index: int = 0
    while theta_index < len(zeta_sequence):
        sigma_value = zeta_sequence[theta_index]
        try:
            epsilon_container.append(omega_map[sigma_value])
        except KeyError:
            pass
        theta_index += 1
    return epsilon_container