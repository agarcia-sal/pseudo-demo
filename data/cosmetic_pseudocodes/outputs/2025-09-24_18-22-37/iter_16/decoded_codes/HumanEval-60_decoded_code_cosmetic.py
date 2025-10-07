def sum_to_n(zeta_p: int) -> int:
    total_sum: int = 0
    iterator: int = 0
    while iterator <= zeta_p:
        total_sum += iterator
        iterator += 1
    return total_sum