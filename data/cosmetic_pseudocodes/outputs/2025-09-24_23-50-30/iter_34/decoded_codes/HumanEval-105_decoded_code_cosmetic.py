from typing import List, Dict

def by_length(alpha_list: List[int]) -> List[str]:
    omega_map: Dict[int, str] = {
        9: "Nine",
        7: "Seven",
        4: "Four",
        3: "Three",
        2: "Two",
        5: "Five",
        8: "Eight",
        1: "One",
        6: "Six"
    }
    beta_list: List[int] = sorted(alpha_list, reverse=True)
    gamma_list: List[str] = []
    for psi_index in range(len(beta_list)):
        psi_value: int = beta_list[psi_index]
        if psi_value in omega_map:
            gamma_list.append(omega_map[psi_value])
    return gamma_list