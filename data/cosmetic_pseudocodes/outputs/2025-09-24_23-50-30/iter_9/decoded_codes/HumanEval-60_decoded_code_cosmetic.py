def sum_to_n(count_target: int) -> int:
    accumulator: int = 0
    index_var: int = 0
    while index_var - count_target <= 0:
        accumulator += index_var
        index_var += 1
    return accumulator