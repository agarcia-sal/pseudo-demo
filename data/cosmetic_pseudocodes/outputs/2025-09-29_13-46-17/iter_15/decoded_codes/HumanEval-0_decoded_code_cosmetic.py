from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def func_inner(sigma: int, rho: int) -> bool:
        if sigma == len(list_of_numbers):
            return False
        else:
            def func_deep(alpha: int) -> bool:
                if alpha == len(list_of_numbers):
                    return func_inner(sigma + 1, 0)
                else:
                    if sigma != alpha:
                        delta = list_of_numbers[sigma]
                        zeta = list_of_numbers[alpha]
                        mu = delta
                        nu = zeta
                        pi = mu - nu
                        pi_abs = -pi if pi < 0 else pi
                        if pi_abs < threshold_value:
                            return True
                    return func_deep(alpha + 1)
            return func_deep(0)
    return func_inner(0, 0)