from functools import cache

@cache
def fibfib(quantity_k: int) -> int:
    if quantity_k not in {0, 1, 2}:
        return fibfib(quantity_k - 3) + fibfib(quantity_k - 2) + fibfib(quantity_k - 1)
    if quantity_k == 2:
        return 1
    return 0