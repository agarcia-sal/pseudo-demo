def sum_to_n(num: int) -> int:
    total = 0
    counter = 0
    while counter <= num:
        total += counter
        counter += 1
    return total