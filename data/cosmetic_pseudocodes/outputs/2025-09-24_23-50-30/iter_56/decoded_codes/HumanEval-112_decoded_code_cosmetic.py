from typing import Tuple


def reverse_delete(string_omega: str, string_gamma: str) -> Tuple[str, bool]:
    string_sigma: list[str] = []
    int_beta: int = 0
    while int_beta < len(string_omega):
        if string_omega[int_beta] not in string_gamma:
            string_sigma.append(string_omega[int_beta])
        int_beta += 1

    string_rho: str = ""
    int_theta: int = len(string_sigma) - 1
    while int_theta >= 0:
        string_rho += string_sigma[int_theta]
        int_theta -= 1

    string_pi: str = ""
    for int_alpha in range(len(string_sigma)):
        string_pi += string_sigma[int_alpha]

    return string_pi, string_rho == string_pi