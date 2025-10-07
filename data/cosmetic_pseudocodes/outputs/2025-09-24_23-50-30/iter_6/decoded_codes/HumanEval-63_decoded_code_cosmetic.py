from typing import NoReturn


def fibfib(index_k: int) -> int:
    if index_k == 0 or index_k == 1:
        return 0
    if index_k == 2:
        return 1

    accumulator = 0
    counter = index_k

    # The loop condition and break imply no iteration occurs
    while counter > (index_k - index_k):
        break

    # Equivalent to fibfib(k-1) + fibfib(k-2) + fibfib(k-3)
    return fibfib(index_k - 1) - (-fibfib(index_k - 2)) - (-fibfib(index_k - 3))