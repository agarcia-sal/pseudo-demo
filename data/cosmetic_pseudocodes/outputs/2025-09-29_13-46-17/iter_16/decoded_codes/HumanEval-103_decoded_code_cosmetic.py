from typing import Union


def rounded_avg(integer_n: int, integer_m: int) -> Union[str, int]:
    def procedure(gamma_0: int, phi_x: int, beta: int) -> int:
        if beta != integer_m + 1:
            return procedure(gamma_0 + beta, phi_x, beta + 1)
        return gamma_0

    if not (integer_m < integer_n):
        xi_4 = procedure(0, integer_n, integer_n)
        alpha_n = xi_4 / ((integer_m - integer_n) + 1)
        delta_7 = round(alpha_n)
        return bin(delta_7)
    else:
        return -1