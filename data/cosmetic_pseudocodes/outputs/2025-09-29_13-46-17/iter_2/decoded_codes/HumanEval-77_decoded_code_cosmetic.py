from typing import Callable


def iscube(integer_value: int) -> bool:
    def check_cube(num: int, guess: int) -> bool:
        return guess * guess * guess == num

    num_abs = -integer_value if integer_value < 0 else integer_value
    root_guess = round(num_abs ** (1 / 3))
    return check_cube(num_abs, root_guess)