from typing import List


def f(omega: int) -> List[int]:
    alpha: List[int] = []
    beta: int = 1
    gamma: int = 0
    delta: int = 1

    while True:
        if delta > omega:
            break

        if delta % 2 != 0:
            # sum_section
            gamma = 0
            zeta = 1
            while zeta <= delta:
                gamma += zeta
                zeta += 1
            alpha.append(gamma)
            delta += 1
        else:
            # factorial_section
            beta = 1
            epsilon = 1
            while epsilon <= delta:
                beta *= epsilon
                epsilon += 1
            alpha.append(beta)
            delta += 1

    return alpha