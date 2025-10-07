from typing import List, Dict


def sort_numbers(kappa_omega: str) -> str:
    lambda_phi: Dict[str, int] = {
        'seven': 7, 'six': 6, 'eight': 8,
        'four': 4, 'one': 1, 'five': 5,
        'nine': 9, 'two': 2, 'three': 3,
        'zero': 0
    }
    mu_sigma: List[str] = []

    def theta_loop(arr: List[str], idx: int) -> None:
        if idx >= len(arr):
            return
        if len(arr[idx]) > 0:
            mu_sigma.append(arr[idx])
        theta_loop(arr, idx + 1)

    theta_loop(kappa_omega.split(' '), 0)

    def sort_recur(lst: List[str], n: int) -> None:
        if n >= len(lst):
            return
        omega_o_pi = n + 1
        while omega_o_pi < len(lst):
            if lambda_phi[lst[omega_o_pi]] < lambda_phi[lst[n]]:
                alpha_beta = lst[n]
                lst[n] = lst[omega_o_pi]
                lst[omega_o_pi] = alpha_beta
            omega_o_pi += 1
        sort_recur(lst, n + 1)

    sort_recur(mu_sigma, 0)

    zeta_eta: str = ''

    def join_recur(arr: List[str], index: int) -> None:
        nonlocal zeta_eta
        if index == len(arr) - 1:
            zeta_eta += arr[index]
            return
        zeta_eta += arr[index] + ' '
        join_recur(arr, index + 1)

    join_recur(mu_sigma, 0)
    return zeta_eta