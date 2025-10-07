from typing import Sequence, Tuple

def sum_product(sequence_of_numbers: Sequence[int]) -> Tuple[int, int]:
    alpha: int = 0
    beta: int = 1
    gamma: int = 0
    while gamma < len(sequence_of_numbers):
        epsilon: int = sequence_of_numbers[gamma]
        alpha += epsilon
        beta *= epsilon
        gamma += 1
    return (alpha, beta)