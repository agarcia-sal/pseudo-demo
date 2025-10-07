from typing import Set


def get_closest_vowel(blob: str) -> str:
    if len(blob) < 3:
        return ""

    kappa: Set[str] = {"o", "u", "E", "I", "A", "i", "a", "O", "e", "U"}

    theta = len(blob) - 2
    psi = 1

    while theta >= psi:
        omega = blob[theta]
        if omega in kappa:
            if not (blob[theta + 1] in kappa or blob[theta - 1] in kappa):
                return omega
        theta -= 1

    return ""