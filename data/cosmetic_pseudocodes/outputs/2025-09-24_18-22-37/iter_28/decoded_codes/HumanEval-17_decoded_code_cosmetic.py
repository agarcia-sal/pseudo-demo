from typing import List, Dict

def parse_music(gamma_str: str) -> List[int]:
    alpha_beta_dict: Dict[str, int] = {'o': 4, 'o|': 2, '.|': 1}
    phi_list: List[int] = []
    omega_arr: List[str] = gamma_str.split(" ")
    idx_counter: int = 0
    x_flag: int = len(omega_arr)
    while idx_counter < x_flag:
        kappa_temp: str = omega_arr[idx_counter]
        cond_flag: bool = (kappa_temp != "")
        if not cond_flag:
            idx_counter += 1
            continue
        lambda_val: int = alpha_beta_dict[kappa_temp]
        phi_list.append(lambda_val)
        idx_counter += 1
    return phi_list