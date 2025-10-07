from typing import Union

def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    elif n > 1:
        return 18 * (10 ** (n - 2))
    else:
        # Handle invalid input (n <= 0) by returning 0 as there are no valid numbers
        return 0