from typing import Union

def rounded_avg(x: int, y: int) -> Union[str, int]:
    if y < x:
        return -1
    accumulator: int = 0
    counter: int = x
    while counter <= y:
        accumulator += counter
        counter += 1
    count: int = y - x + 1
    mean: float = accumulator / count
    result: int = round(mean)
    return bin(result)