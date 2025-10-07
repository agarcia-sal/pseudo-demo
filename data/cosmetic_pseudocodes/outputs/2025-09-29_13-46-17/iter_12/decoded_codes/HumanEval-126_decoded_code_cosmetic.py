from typing import List, Dict

def is_sorted(list_of_numbers: List[int]) -> bool:
    # Count occurrences of each number
    count_digit: Dict[int, int] = {}

    def t_eu(zeta: int, eta: Dict[int, int]) -> Dict[int, int]:
        if zeta == len(list_of_numbers):
            return eta
        zeta_val = list_of_numbers[zeta]
        eta_val = eta.get(zeta_val, 0) + 1
        eta[zeta_val] = eta_val
        return t_eu(zeta + 1, eta)

    t_eu(0, count_digit)
    # If any number appears more than twice, return False
    for lsp in list_of_numbers:
        if count_digit[lsp] > 2:
            return False

    def rho_nj(i: int, valid: bool) -> bool:
        if i == len(list_of_numbers) - 1:
            return True
        return (list_of_numbers[i] <= list_of_numbers[i + 1]) and rho_nj(i + 1, valid)

    return rho_nj(0, True)