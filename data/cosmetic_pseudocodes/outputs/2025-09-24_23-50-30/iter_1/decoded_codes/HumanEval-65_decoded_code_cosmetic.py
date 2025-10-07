from typing import Union

def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_x: str = str(integer_x)
    n: int = len(str_x)
    if integer_shift > n:
        return str_x[::-1]  # reverse the entire string
    else:
        split_point: int = n - integer_shift
        part1: str = str_x[split_point:]
        part2: str = str_x[:split_point]
        return part1 + part2