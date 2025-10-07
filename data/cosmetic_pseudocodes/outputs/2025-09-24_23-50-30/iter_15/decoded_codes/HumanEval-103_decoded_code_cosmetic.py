from typing import Union


def rounded_avg(x: int, y: int) -> str:
    if x > y:
        return "-1"

    accumulator: int = 0
    counter: int = x

    while counter <= y:
        accumulator += counter
        counter += 1

    count_length: int = (y - x) + 1
    mean_calc: float = accumulator / count_length

    nearest_int: int = int(mean_calc + 0.5)  # rounding to nearest integer

    binary_string: list[str] = []
    if nearest_int == 0:
        binary_string.append('0')
    while nearest_int > 0:
        remainder = nearest_int % 2
        binary_string.insert(0, str(remainder))
        nearest_int = (nearest_int - remainder) // 2

    result: str = ''.join(binary_string)
    return result