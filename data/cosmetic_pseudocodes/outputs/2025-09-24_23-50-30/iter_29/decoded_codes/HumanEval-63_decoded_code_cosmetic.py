from typing import Callable

def fibfib(scalar_p: int) -> int:
    if scalar_p in (0, 1):
        return 0
    if scalar_p == 2:
        return 1

    def inner_loop(accu_x: int, accu_y: int, accu_z: int, counter_q: int) -> int:
        if counter_q == scalar_p:
            return accu_z
        return inner_loop(accu_y, accu_z, accu_x + accu_y + accu_z, counter_q + 1)

    return inner_loop(0, 0, 1, 2)