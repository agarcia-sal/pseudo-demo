from typing import Union

def car_race_collision(n: Union[int, float]) -> Union[int, float]:
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be an int or float")
    return n ** 2