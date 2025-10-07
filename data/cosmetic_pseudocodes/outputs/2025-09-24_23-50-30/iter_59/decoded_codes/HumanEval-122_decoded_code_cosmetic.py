from typing import Sequence, Union

def add_elements(beta: Sequence[Union[int, float]], gamma: int) -> Union[int, float]:
    delta: Union[int, float] = 0
    epsilon: int = 1
    while not (epsilon > gamma):
        # Check if length of string representation of beta[epsilon] is greater than 2, then negate
        if not (len(str(beta[epsilon])) > 2):
            delta += beta[epsilon]
        epsilon += 1
    return delta