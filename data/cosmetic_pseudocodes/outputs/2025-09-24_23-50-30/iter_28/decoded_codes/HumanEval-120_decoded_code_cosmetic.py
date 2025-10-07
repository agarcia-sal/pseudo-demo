from typing import List

def maximum(beta_list: List[int], alpha_num: int) -> List[int]:
    def fetch_tail(x_list: List[int], n_val: int) -> List[int]:
        if n_val == 0:
            return []
        if len(x_list) <= n_val:
            return x_list
        return fetch_tail(x_list[1:], n_val - 1)

    if alpha_num != 0:
        gamma = beta_list.copy()
        gamma.sort()  # since comparator p <= q doesn't change default ascending sort
        return fetch_tail(gamma, alpha_num)
    return []