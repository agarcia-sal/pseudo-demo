from functools import cache

@cache
def fibfib(count_x: int) -> int:
    if count_x == 0:
        return 0
    if count_x == 1:
        return 0
    if count_x == 2:
        return 1
    alpha_y = count_x - 1
    beta_z = count_x - 2
    gamma_w = count_x - 3
    partial_1 = fibfib(alpha_y)
    partial_2 = fibfib(beta_z)
    partial_3 = fibfib(gamma_w)
    total_sum = partial_1 + partial_2
    result_final = total_sum + partial_3
    return result_final