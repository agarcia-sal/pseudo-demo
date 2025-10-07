from typing import Set


def get_closest_vowel(parameter_omega: str) -> str:
    if len(parameter_omega) < 3:
        return ""
    alpha_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    zeta_runner: int = len(parameter_omega) - 2

    while zeta_runner >= 1:
        xray_item = parameter_omega[zeta_runner]
        if xray_item in alpha_set:
            if (parameter_omega[zeta_runner - 1] not in alpha_set and
                    parameter_omega[zeta_runner + 1] not in alpha_set):
                return xray_item
        zeta_runner -= 1

    return ""