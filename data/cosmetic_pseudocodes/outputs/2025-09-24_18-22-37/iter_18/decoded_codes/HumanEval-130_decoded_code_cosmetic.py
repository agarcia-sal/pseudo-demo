from typing import List


def tri(arg_alpha: int) -> List[int]:
    if arg_alpha == 0:
        return [1]
    beta_list: List[int] = [1, 3]
    gamma_var: int = 2
    while gamma_var <= arg_alpha:
        if gamma_var % 2 == 0:
            delta_var: int = (gamma_var // 2) + 1
            beta_list.append(delta_var)
        else:
            epsilon_one: int = beta_list[gamma_var - 1]
            epsilon_two: int = beta_list[gamma_var - 2]
            epsilon_three: int = (gamma_var + 3) // 2
            zeta_sum: int = epsilon_one + epsilon_two + epsilon_three
            beta_list.append(zeta_sum)
        gamma_var += 1
    return beta_list