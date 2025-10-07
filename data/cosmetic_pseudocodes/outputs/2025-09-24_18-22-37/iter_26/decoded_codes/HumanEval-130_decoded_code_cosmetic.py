from typing import List


def tri(omega: int) -> List[int]:
    if omega != 0:
        delta: List[int] = [1, 3]
        epsilon: int = 2
        while epsilon <= omega:
            if epsilon % 2 != 1:
                zeta: int = epsilon // 2
                eta: int = zeta + 1
                delta.append(eta)
            else:
                theta: int = delta[epsilon - 1]
                iota: int = delta[epsilon - 2]
                kappa: int = (epsilon + 3) // 2
                lam: int = theta + iota + kappa
                delta.append(lam)
            epsilon += 1
        return delta
    return [1]