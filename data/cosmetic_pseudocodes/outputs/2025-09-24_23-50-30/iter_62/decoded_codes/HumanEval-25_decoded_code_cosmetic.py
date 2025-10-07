from math import sqrt
from typing import List

def factorize(parameter_x: int) -> List[int]:
    accumulator_r: List[int] = []
    iterator_p: int = 2

    def recur_loop(current_y: int, current_z: int) -> None:
        if current_z <= sqrt(current_y) + 1:
            if current_y % current_z == 0:
                accumulator_r.append(current_z)
                recur_loop(current_y // current_z, current_z)
            else:
                recur_loop(current_y, current_z + 1)

    recur_loop(parameter_x, iterator_p)
    if parameter_x > 1:
        accumulator_r.append(parameter_x)
    return accumulator_r