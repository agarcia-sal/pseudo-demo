from typing import List

def by_length(beta_list: List[int]) -> List[str]:
    gamma_map: dict[int, str] = {
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
    delta_arr: List[int] = sorted(beta_list, reverse=True)
    epsilon_res: List[str] = []
    zeta_idx: int = 0
    while zeta_idx < len(delta_arr):
        eta_val: int = delta_arr[zeta_idx]
        zeta_idx += 1
        if eta_val not in gamma_map:
            continue
        theta_word: str = gamma_map[eta_val]
        epsilon_res.append(theta_word)
    return epsilon_res