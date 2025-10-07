from typing import Union

def choose_num(number_x: int, number_y: int) -> int:
    if number_x > number_y:
        return -1
    if number_y % 2 == 0:
        return number_y
    if number_x == number_y:
        return -1
    return number_y - 1