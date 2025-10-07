from typing import Union

def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    else:
        return 18 * (10 ** (n - 2))