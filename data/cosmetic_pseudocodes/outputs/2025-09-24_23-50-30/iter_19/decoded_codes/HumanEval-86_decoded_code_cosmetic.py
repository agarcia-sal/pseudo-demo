from typing import List


def anti_shuffle(alpha: str) -> str:
    beta: List[str] = alpha.split(' ')
    gamma: List[str] = []
    k: int = 0
    while k < len(beta):
        phi: str = beta[k]
        theta: List[str] = list(phi)
        i: int = 0
        while i < len(theta) - 1:
            j: int = i + 1
            while j < len(theta):
                if theta[i] > theta[j]:
                    theta[i], theta[j] = theta[j], theta[i]  # swap characters
                j += 1
            i += 1
        psi: str = ''.join(theta)
        gamma.append(psi)
        k += 1
    delta: str = ''
    m: int = 0
    while m < len(gamma):
        delta += gamma[m]
        if m < len(gamma) - 1:
            delta += ' '
        m += 1
    return delta