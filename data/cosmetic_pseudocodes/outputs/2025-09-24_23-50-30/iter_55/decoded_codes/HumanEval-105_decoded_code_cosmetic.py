from typing import List, Dict

def by_length(alpha_list: List[int]) -> List[str]:
    beta_map: Dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }
    rho_list: List[int] = sorted(alpha_list, reverse=True)
    omega_list: List[str] = []

    def iter_gamma(indices: List[int]) -> None:
        if not indices:
            return
        ix, rest_ix = indices[0], indices[1:]
        if ix in beta_map:
            omega_list.append(beta_map[ix])
        iter_gamma(rest_ix)

    iter_gamma(rho_list)
    return omega_list