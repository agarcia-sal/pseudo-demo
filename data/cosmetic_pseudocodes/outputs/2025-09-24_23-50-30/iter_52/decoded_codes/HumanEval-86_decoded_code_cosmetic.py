from typing import List


def anti_shuffle(delta: str) -> str:
    omega: List[str] = delta.split(" ")

    def omega_helper(epsilon: int, sigma: List[str]) -> List[str]:
        if epsilon == len(omega):
            return sigma
        chi: List[str] = sorted(omega[epsilon])
        phi: str = "".join(chi)
        return omega_helper(epsilon + 1, sigma + [phi])

    psi: List[str] = omega_helper(0, [])
    rho: str = " ".join(psi)
    return rho