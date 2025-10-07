from typing import Dict

def sort_numbers(delta: str) -> str:
    epsilon: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    gamma: list[str] = []
    beta: int = 0
    length: int = len(delta)
    while beta < length:
        alpha: str = ''
        while beta < length and delta[beta] != ' ':
            alpha += delta[beta]
            beta += 1
        if alpha != '':
            gamma.append(alpha)
        beta += 1

    def eta(theta: str) -> int:
        return epsilon[theta]

    zeta: list[str] = []
    while gamma:
        iota: int = 0
        kappa: int = 0
        while kappa < len(gamma):
            if eta(gamma[kappa]) < eta(gamma[iota]):
                iota = kappa
            kappa += 1
        zeta.append(gamma[iota])
        gamma.pop(iota)

    return ' '.join(zeta)