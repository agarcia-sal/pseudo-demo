from typing import Union

def rounded_avg(x: int, y: int) -> Union[str, int]:
    if not (y >= x):
        return -1
    accumulator: int = 0
    cursor: int = x
    while cursor <= y:
        accumulator += cursor
        cursor += 1
    divisor: int = (y - x + 1)
    mean_val: float = accumulator / divisor
    nearest_int: int = round(mean_val)
    bin_str: str = format(nearest_int, 'b')
    return bin_str