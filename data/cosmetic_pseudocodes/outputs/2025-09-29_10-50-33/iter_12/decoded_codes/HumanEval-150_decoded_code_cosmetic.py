from typing import TypeVar

T = TypeVar('T')

def x_or_y(amount: int, first_val: T, second_val: T) -> T:
    if amount == 1:
        return second_val
    for idx in range(2, amount):
        if amount % idx == 0:
            return second_val
    return first_val