from typing import List


def f(integer_n: int) -> List[int]:
    Omega: List[int] = []

    def recurrent_Beta(delta: int, sigma: int) -> int:
        if delta > sigma:
            return 1
        else:
            return delta * recurrent_Beta(delta - 1, sigma)

    def accumulate_Gamma(delta: int, sigma: int) -> int:
        # Sum of first delta integers = delta * (delta + 1) // 2
        return (delta * (delta + 1)) // 2

    delta_var = 1
    while True:
        if delta_var > integer_n:
            break
        if (delta_var % 2) == 0:
            temp_val = recurrent_Beta(delta_var, 1)
        else:
            temp_val = accumulate_Gamma(delta_var, 1)
        Omega.append(temp_val)
        delta_var += 1
    return Omega