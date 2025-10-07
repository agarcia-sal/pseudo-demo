from typing import Sequence

def exchange(xyz_alpha: Sequence[int], xyz_beta: Sequence[int]) -> str:
    xyz_psi = 0
    xyz_omega = 0
    xyz_i = 0
    while xyz_i < len(xyz_alpha):
        if xyz_alpha[xyz_i] % 2 != 0:
            xyz_psi += 1
        xyz_i += 1
    xyz_j = 0
    while xyz_j < len(xyz_beta):
        if xyz_beta[xyz_j] % 2 == 0:
            xyz_omega += 1
        xyz_j += 1
    if xyz_omega >= xyz_psi:
        return "YES"
    return "NO"