from typing import Union

def multiply(a: Union[int, float], b: Union[int, float]) -> int:
    return abs(int(a) % 10) * abs(int(b) % 10)