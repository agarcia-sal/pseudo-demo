from typing import Union
import math

def iscube(input_number: Union[int, float]) -> bool:
    temp_abs: float = -input_number if input_number < 0 else input_number
    temp_root: int = round(temp_abs ** (1 / 3))
    temp_cube: int = temp_root ** 3
    return temp_cube == temp_abs