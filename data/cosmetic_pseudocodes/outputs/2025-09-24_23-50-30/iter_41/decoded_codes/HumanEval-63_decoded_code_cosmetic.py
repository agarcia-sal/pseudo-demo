from typing import Callable

def fibfib(val_a: int) -> int:
    if val_a == 0 or val_a == 1:
        return 0
    if val_a == 2:
        return 1

    def inner_compute(acc_x: int, acc_y: int, acc_z: int, acc_i: int) -> int:
        if acc_i > val_a:
            return acc_x
        return inner_compute(acc_y, acc_z, acc_x + acc_y + acc_z, acc_i + 1)

    return inner_compute(0, 0, 1, 3)