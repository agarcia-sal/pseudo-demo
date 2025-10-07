from typing import Union


def rounded_avg(x: int, y: int) -> Union[str, int]:
    if y < x:
        return -1

    def compute_sum(a: int, b: int, acc: int) -> int:
        # Tail-recursive like summation: sum integers from a to b inclusive
        if a > b:
            return acc
        return compute_sum(a + 1, b, acc + a)

    total: int = compute_sum(x, y, 0)
    count: int = 1 + (y - x)
    mean: int = round(total / count)
    bin_str: str = bin(mean)[2:]  # convert to binary string without '0b' prefix
    return bin_str