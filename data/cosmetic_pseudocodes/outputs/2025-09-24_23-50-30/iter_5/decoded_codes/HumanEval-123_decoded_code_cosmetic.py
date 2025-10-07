from typing import List


def get_odd_collatz(alpha: int) -> List[int]:
    def loop(beta: int, gamma: List[int]) -> List[int]:
        if beta <= 1:
            return gamma
        delta = (beta // 2) * (1 - (beta % 2)) + ((3 * beta + 1) * (beta % 2))
        if delta % 2 == 1:
            return loop(delta, gamma + [delta])
        return loop(delta, gamma)

    epsilon: List[int] = [] if alpha % 2 == 0 else [alpha]
    zeta = loop(alpha, epsilon)
    return sorted(zeta)