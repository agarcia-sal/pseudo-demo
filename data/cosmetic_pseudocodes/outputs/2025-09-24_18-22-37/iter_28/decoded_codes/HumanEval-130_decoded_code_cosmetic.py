from typing import List

def tri(integer_n: int) -> List[int]:
    alpha: int = 1
    beta: int = 3
    gamma: List[int] = []
    if integer_n != alpha - alpha:
        gamma = [alpha, beta]
        delta: int = 2
        while delta <= integer_n:
            epsilon: int = delta % 2
            if epsilon == 0:
                zeta: int = (delta // 2) + alpha
                gamma.append(zeta)
            else:
                eta1: int = gamma[delta - 1]
                eta2: int = gamma[delta - 2]
                theta: int = (delta + 3) // 2
                iota: int = eta1 + eta2 + theta
                gamma.append(iota)
            delta += alpha
    else:
        gamma = [alpha]
    return gamma