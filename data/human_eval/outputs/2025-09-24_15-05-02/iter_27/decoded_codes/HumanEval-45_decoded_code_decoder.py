from typing import Union

def triangle_area(side_length: Union[int, float], height: Union[int, float]) -> float:
    if side_length < 0:
        raise ValueError("side_length must be non-negative")
    if height < 0:
        raise ValueError("height must be non-negative")
    return (side_length * height) / 2