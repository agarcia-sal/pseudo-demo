from typing import Union

def is_simple_power(number: Union[int, float], base: Union[int, float]) -> bool:
    if base == 1:
        return number == 1
    power_value = 1
    while power_value < number:
        power_value *= base
    return power_value == number