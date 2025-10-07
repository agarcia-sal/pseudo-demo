def sum_to_n(num_limit: int) -> int:
    total_sum = 0
    iterator = 0
    while iterator <= num_limit:
        total_sum += iterator
        iterator += 1
    return total_sum