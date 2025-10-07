from typing import List


def words_string(delta: str) -> List[str]:
    omega_list: List[str] = []
    if delta:
        sigma: int = 0
        while sigma < len(delta):
            tau: str = delta[sigma]
            if tau == ",":
                omega_list.append(" ")
            else:
                omega_list.append(tau)
            sigma += 1

        epsilon: str = ""
        kappa: int = 0
        while kappa < len(omega_list):
            epsilon += omega_list[kappa]
            kappa += 1

        zeta_list: List[str] = []
        theta: str = ""
        iota: int = 0
        while iota < len(epsilon):
            char: str = epsilon[iota]
            if char == " ":
                if theta != "":
                    zeta_list.append(theta)
                    theta = ""
            else:
                theta += char
            iota += 1
        if theta != "":
            zeta_list.append(theta)
        return zeta_list
    else:
        return []