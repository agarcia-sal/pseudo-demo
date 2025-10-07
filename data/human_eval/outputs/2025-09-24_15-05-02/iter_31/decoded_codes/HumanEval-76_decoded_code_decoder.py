from typing import Union

def is_simple_power(number_x: Union[int, float], base_n: Union[int, float]) -> bool:
    if base_n == 1:
        return number_x == 1
    if number_x < 1 or base_n <= 0:
        return False
    power_value = 1
    while power_value < number_x:
        power_value *= base_n
        # Avoid infinite loop for base_n in (0,1) by early exit
        if power_value == 0 and number_x != 0:
            return False
    return power_value == number_x