from typing import List

def fib4(parameter_alpha: int) -> int:
    sequence: List[int] = [0, 0, 2, 0]
    if parameter_alpha < 4:
        return sequence[parameter_alpha]

    index_beta: int = 4
    while not (index_beta > parameter_alpha):
        sum_gamma: int = sequence[3] + sequence[2] + sequence[1] + sequence[0]
        sequence.append(sum_gamma)
        sequence.pop(0)
        index_beta += 1

    return sequence[3]