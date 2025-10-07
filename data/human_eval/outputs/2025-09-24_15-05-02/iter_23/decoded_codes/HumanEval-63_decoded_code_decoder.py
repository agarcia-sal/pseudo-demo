from typing import Optional

def fibfib(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    # Compute recursively according to the definition
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)