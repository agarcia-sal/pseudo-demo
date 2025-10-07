from typing import Union

def rounded_avg(a: int, b: int) -> Union[str, int]:
    if not a <= b:
        return -1

    def recursion_sum(x: int, y: int, total: int) -> int:
        if x > y:
            return total
        else:
            return recursion_sum(x + 1, y, total + x)

    accumulator: int = recursion_sum(a, b, 0)
    count: int = b - a + 1
    mean: float = accumulator / count
    nearest: int = round(mean)
    bin_form: str = bin(nearest)
    return bin_form