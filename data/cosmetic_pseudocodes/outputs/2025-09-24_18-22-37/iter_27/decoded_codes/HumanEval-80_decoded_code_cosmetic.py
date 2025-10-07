from typing import Sequence, Any

def is_happy(input_value: Sequence[Any]) -> bool:
    omega: int = len(input_value)
    if omega < 3:
        return False
    gamma: int = 0
    while gamma <= omega - 3:
        delta = input_value[gamma]
        epsilon = input_value[gamma + 1]
        zeta = input_value[gamma + 2]
        cond1 = delta == epsilon
        cond2 = epsilon == zeta
        cond3 = delta == zeta
        if cond1 or cond2 or cond3:
            return False
        gamma += 1
    return True