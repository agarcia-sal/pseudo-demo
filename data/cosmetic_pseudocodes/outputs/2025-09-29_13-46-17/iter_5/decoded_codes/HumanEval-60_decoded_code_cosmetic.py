def sum_to_n(N: int) -> int:
    accumulator = 0
    index_var = 0
    while index_var <= N:
        accumulator += index_var
        index_var += 1
    return accumulator