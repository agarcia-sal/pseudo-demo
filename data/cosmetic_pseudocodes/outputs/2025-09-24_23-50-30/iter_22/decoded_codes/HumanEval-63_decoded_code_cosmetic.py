from functools import lru_cache

@lru_cache(maxsize=None)
def fibfib(number_k: int) -> int:
    if number_k == 0 or number_k == 1:
        return 0
    if number_k == 2:
        return 1
    idx_p = number_k - 1
    idx_q = number_k - 2
    idx_r = number_k - 3
    return fibfib(idx_p) + fibfib(idx_q) + fibfib(idx_r)