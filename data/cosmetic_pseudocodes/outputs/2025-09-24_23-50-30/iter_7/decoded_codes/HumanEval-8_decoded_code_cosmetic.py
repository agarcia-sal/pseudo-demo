from typing import Sequence, Tuple

def sum_product(sequence_of_ints: Sequence[int]) -> Tuple[int, int]:
    alpha: int = 1
    beta: int = 0

    def recur(index: int, beta: int = beta, alpha: int = alpha) -> Tuple[int, int]:
        if index >= len(sequence_of_ints):
            return beta, alpha
        gamma = sequence_of_ints[index]
        delta = alpha * gamma
        epsilon = beta + gamma
        return recur(index + 1, beta=epsilon, alpha=delta)

    return recur(0)