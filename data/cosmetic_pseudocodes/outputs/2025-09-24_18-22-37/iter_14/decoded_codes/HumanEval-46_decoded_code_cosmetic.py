from typing import List

def fib4(omega: int) -> int:
    theta: List[int] = [0, 0, 2, 0]
    if omega < 4:
        return theta[omega]

    psi = 4
    while psi <= omega:
        alpha = theta[3]
        beta = theta[2]
        gamma = theta[1]
        delta = theta[0]
        epsilon = alpha + beta + gamma + delta

        theta.append(epsilon)
        theta.pop(0)

        psi += 1

    return theta[3]