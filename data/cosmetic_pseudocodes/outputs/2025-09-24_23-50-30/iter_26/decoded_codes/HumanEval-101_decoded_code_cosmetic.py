from typing import List


def words_string(phi: str) -> List[str]:
    if phi == "":
        return []

    omega: List[str] = []

    beta = 0
    while beta < len(phi):
        if phi[beta] == ',':
            omega.append(' ')
        else:
            omega.append(phi[beta])
        beta += 1

    gamma = ""
    delta = 0
    while delta < len(omega):
        gamma += omega[delta]
        delta += 1

    return [e for e in gamma.split(' ') if e != ""]