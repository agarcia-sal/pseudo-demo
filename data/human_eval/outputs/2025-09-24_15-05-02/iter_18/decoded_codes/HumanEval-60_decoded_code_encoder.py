from typing import Union

def sum_to_n(n: Union[int, float]) -> int:
    if not isinstance(n, int):
        if isinstance(n, float) and n.is_integer():
            n = int(n)
        else:
            raise ValueError("Input must be an integer or integer-equivalent float")
    if n < 0:
        raise ValueError("Input must be non-negative")
    return n * (n + 1) // 2