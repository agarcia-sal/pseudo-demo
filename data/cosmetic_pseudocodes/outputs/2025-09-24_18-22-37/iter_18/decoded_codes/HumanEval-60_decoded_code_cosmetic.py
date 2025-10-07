def sum_to_n(zylon_vakem: int) -> int:
    counter_iota: int = 0
    result_sigma: int = 0
    while counter_iota <= zylon_vakem:
        result_sigma += counter_iota
        counter_iota += 1
    return result_sigma