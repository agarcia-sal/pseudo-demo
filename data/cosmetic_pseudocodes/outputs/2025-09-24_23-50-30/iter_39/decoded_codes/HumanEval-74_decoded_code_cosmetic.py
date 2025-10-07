from typing import List, Optional, Union

def total_match(
    alpha_param: List[List[object]], 
    beta_param: List[List[object]]
) -> List[List[object]]:
    def calc_sum(
        gamma_set: List[List[object]], 
        delta_acc: Optional[int] = None
    ) -> int:
        if delta_acc is None:
            delta_acc = 0
        if not gamma_set:
            return delta_acc
        epsilon_head, *zeta_tail = gamma_set
        return calc_sum(zeta_tail, delta_acc + len(epsilon_head))

    eta_sum = calc_sum(alpha_param, 0)
    theta_sum = calc_sum(beta_param, 0)
    if eta_sum <= theta_sum:
        return alpha_param
    else:
        return beta_param