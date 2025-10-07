def sum_to_n(n_val: int) -> int:
    accumulator = 0
    for counter in range(n_val + 1):
        accumulator += counter
    return accumulator