from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Sequence[str])

def total_match(param_alpha: T, param_beta: T) -> T:
    idx_omega: int = 0
    cnt_sigma: int = 0
    l_delta: int = len(param_alpha)
    while idx_omega < l_delta:
        cnt_sigma += len(param_alpha[idx_omega])
        idx_omega += 1

    walker_theta: int = 0
    acc_mu: int = 0
    len_nu: int = len(param_beta)
    while walker_theta < len_nu:
        acc_mu += len(param_beta[walker_theta])
        walker_theta += 1

    return param_alpha if cnt_sigma <= acc_mu else param_beta