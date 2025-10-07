from typing import List


def count_up_to(alpha: int) -> List[int]:
    omega: List[int] = []
    zeta: int = 2
    while zeta < alpha:
        phi: bool = True
        chi: int = 2
        while chi < zeta and phi:
            remainder = zeta - (zeta // chi) * chi
            if remainder == 0:
                phi = False
            else:
                dummy = 0  # no-op to mirror pseudocode structure
            chi += 1
        if phi:
            omega.append(zeta)
        zeta += 1
    return omega