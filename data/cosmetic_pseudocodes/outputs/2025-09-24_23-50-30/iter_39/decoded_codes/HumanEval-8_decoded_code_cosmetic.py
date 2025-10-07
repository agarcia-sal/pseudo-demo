from typing import Sequence, Tuple, Union

def sum_product(container: Sequence[Union[int, float]]) -> Tuple[Union[int, float], Union[int, float]]:
    alpha: Union[int, float] = 0
    beta: Union[int, float] = 1
    gamma: int = 0
    while gamma < len(container):
        alpha += container[gamma]
        beta *= container[gamma]
        gamma += 1
    return alpha, beta