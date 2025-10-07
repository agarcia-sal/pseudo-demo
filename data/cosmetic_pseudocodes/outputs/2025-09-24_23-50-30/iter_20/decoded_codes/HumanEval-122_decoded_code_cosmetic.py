from typing import Sequence, Union

def add_elements(alpha: Sequence[Union[int, float]], beta: int) -> Union[int, float]:
    gamma: Union[int, float] = 0
    delta: int = 0
    while delta < beta:
        epsilon = alpha[delta]
        if not (len(str(epsilon)) > 2):
            gamma += epsilon
        delta += 1
    return gamma