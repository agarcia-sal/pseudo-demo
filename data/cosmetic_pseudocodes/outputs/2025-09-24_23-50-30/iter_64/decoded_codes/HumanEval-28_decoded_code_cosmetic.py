from typing import Sequence

def concatenate(parameter_alpha: Sequence[str]) -> str:
    iterator_beta: int = 0
    accumulator_gamma: str = ""
    while iterator_beta < len(parameter_alpha):
        accumulator_gamma += parameter_alpha[iterator_beta]
        iterator_beta += 1
    return accumulator_gamma