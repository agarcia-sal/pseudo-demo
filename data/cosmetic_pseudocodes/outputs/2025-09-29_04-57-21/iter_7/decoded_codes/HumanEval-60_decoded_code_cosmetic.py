def sum_to_n(p_num: int) -> int:
    total: int = 0
    counter: int = 0
    while counter <= p_num:
        total += counter
        counter += 1
    return total