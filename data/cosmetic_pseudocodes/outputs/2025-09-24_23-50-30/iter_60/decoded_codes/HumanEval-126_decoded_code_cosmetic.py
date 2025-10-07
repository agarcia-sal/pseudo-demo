from typing import List, Dict, Union


def is_sorted(param_alpha: List[int]) -> Union[bool, None]:
    var_beta: Dict[int, int] = {key: 0 for key in param_alpha}

    def proc_gamma(idx_delta: int) -> None:
        if idx_delta == len(param_alpha):
            return
        var_beta[param_alpha[idx_delta]] += 1
        proc_gamma(idx_delta + 1)

    proc_gamma(0)

    def proc_eta(lst_theta: List[int], idx_iota: int, acc_kappa: Union[bool, None]) -> Union[bool, None]:
        if idx_iota == len(lst_theta):
            return acc_kappa
        if not (var_beta[lst_theta[idx_iota]] <= 2):
            return False
        return proc_eta(lst_theta, idx_iota + 1, acc_kappa)

    var_lambda = proc_eta(param_alpha, 0, True)
    if var_lambda is False:
        return False

    def proc_mu(arr_nu: List[int], idx_xi: int, flag_omicron: bool) -> bool:
        if idx_xi == len(arr_nu):
            return flag_omicron
        if not (arr_nu[idx_xi - 1] <= arr_nu[idx_xi]):
            flag_omicron = False
        return proc_mu(arr_nu, idx_xi + 1, flag_omicron)

    return proc_mu(param_alpha, 1, True)