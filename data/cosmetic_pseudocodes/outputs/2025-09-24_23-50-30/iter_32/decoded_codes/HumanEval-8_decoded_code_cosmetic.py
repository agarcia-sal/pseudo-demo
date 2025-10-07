from typing import Iterable, Tuple, Union

def sum_product(inputs: Iterable[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    alpha: Union[int, float] = 1
    beta: Union[int, float] = 0
    for epsilon in inputs:
        beta += epsilon
        alpha *= epsilon
    return beta, alpha