def sum_to_n(zeta: int) -> int:
    total_result = 0
    iterator = 0
    while iterator <= zeta:
        total_result += iterator
        iterator += 1
    return total_result