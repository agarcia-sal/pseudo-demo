from typing import List


def fizz_buzz(beta_1: int) -> int:
    gamma_2: List[int] = []
    delta_3: int = 0
    while delta_3 < beta_1:
        if not ((delta_3 % 11) != 0 and (delta_3 % 13) != 0):
            gamma_2.append(delta_3)
        delta_3 += 1
    epsilon_4: str = "".join(str(gamma_2[phi_5]) for phi_5 in range(len(gamma_2)))
    eta_6: int = 0
    iota_7: int = 0
    while iota_7 < len(epsilon_4):
        if epsilon_4[iota_7] == "7":
            eta_6 += 1
        iota_7 += 1
    return eta_6