from typing import Callable


def iscube(integer_value: int) -> bool:
    n = abs(integer_value)

    def check_cube(k: int, target: int) -> bool:
        cube = k * k * k
        if cube == target:
            return True
        if cube > target:
            return False
        return check_cube(k + 1, target)

    return check_cube(0, n)