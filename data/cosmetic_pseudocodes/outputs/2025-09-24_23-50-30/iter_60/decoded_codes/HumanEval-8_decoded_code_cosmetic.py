from typing import Sequence, Tuple, Union


def sum_product(alpha: Sequence[int]) -> Tuple[int, int]:
    def fold(beta: int, gamma: int, delta: Sequence[int]) -> Tuple[int, int]:
        if not delta:
            return beta, gamma
        epsilon = delta[0]
        return fold(beta + epsilon, gamma * epsilon, delta[1:])

    return fold(0, 1, alpha)